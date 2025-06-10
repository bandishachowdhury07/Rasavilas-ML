from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from gensim.models import Word2Vec
import numpy as np
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = joblib.load("model_cbow.model")  # Adjust if using pickle or another format 

# Define input schema
class InputData(BaseModel):
    ingredients: str  # Comma-separated list of ingredients
    N: int = 5        # Number of recommendations (optional, default 5)
    mean: bool = False  # Use mean embedding (optional, default False)

def get_and_sort_corpus(data):
    corpus_sorted = []
    for doc in data['Cleaned-Ingredients'].values:
        doc = sorted(doc.split(sep=','))
        corpus_sorted.append(doc)
    return corpus_sorted

class MeanEmbeddingVectoriser(object):
    def __init__(self, model_cbow):
        self.model_cbow = model_cbow
        self.vector_size = model_cbow.wv.vector_size
    def fit(self):
        return self
    def transform(self, docs):
        return self.doc_average_list(docs)
    def doc_average(self, doc):
        mean = []
        for word in doc:
            if word in self.model_cbow.wv.index_to_key:
                mean.append(self.model_cbow.wv.get_vector(word))
        if not mean:
            return np.zeros(self.vector_size)
        else:
            mean = np.array(mean).mean(axis=0)
            return mean
    def doc_average_list(self, docs):
        return np.vstack([self.doc_average(doc) for doc in docs])

class tfidfEmbeddingVectorizer(object):
    def __init__(self, model_cbow):
        self.model_cbow = model_cbow
        self.vector_size = model_cbow.vector_size
        self.word_idf_weight = None
    def fit(self, docs):
        text_docs = [" ".join(doc) for doc in docs]
        tfidf = TfidfVectorizer()
        tfidf.fit(text_docs)
        max_idf = max(tfidf.idf_)
        self.word_idf_weight = defaultdict(lambda: max_idf, [(word, tfidf.idf_[i]) for word, i in tfidf.vocabulary_.items()])
        return self
    def transform(self, docs):
        return self.doc_average_list(docs)
    def doc_average(self, doc):
        mean = []
        for word in doc:
            if word in self.model_cbow.wv.index_to_key:
                mean.append(self.model_cbow.wv.get_vector(word) * self.word_idf_weight[word])
        if not mean:
            return np.zeros(self.vector_size)
        else:
            mean = np.array(mean).mean(axis=0)
            return mean
    def doc_average_list(self, docs):
        return np.vstack([self.doc_average(doc) for doc in docs])

def get_recommendations(N, scores):
    df_recipes = pd.read_csv("Cleaned_Indian_Food_Dataset.csv")
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:N]
    recommendation = pd.DataFrame(columns=["recipe", "ingredients", "url"])
    count = 0
    for i in top:
        recommendation.at[count, "recipe"] = df_recipes["TranslatedRecipeName"][i]
        recommendation.at[count, "ingredients"] = df_recipes["Cleaned-Ingredients"][i]
        recommendation.at[count, "url"] = df_recipes["URL"][i]
        count += 1
    return recommendation

@app.post("/predict")
async def predict(data: InputData):
    try:
        # Load data and model
        df = pd.read_csv("Cleaned_Indian_Food_Dataset.csv")
        model = Word2Vec.load("model_cbow.model")
        corpus = get_and_sort_corpus(df)
        # Choose vectorizer
        if data.mean:
            vec_tr = MeanEmbeddingVectoriser(model)
            doc_vec = vec_tr.transform(corpus)
            doc_vec = [doc.reshape(1, -1) for doc in doc_vec]
        else:
            vec_tr = tfidfEmbeddingVectorizer(model)
            vec_tr.fit(corpus)
            doc_vec = vec_tr.transform(corpus)
            doc_vec = [doc.reshape(1, -1) for doc in doc_vec]
        # Prepare input
        input_ingredients = [i.strip() for i in data.ingredients.split(",") if i.strip()]
        if data.mean:
            input_embedding = vec_tr.transform([input_ingredients])[0].reshape(1, -1)
        else:
            input_embedding = vec_tr.transform([input_ingredients])[0].reshape(1, -1)
        # Cosine similarity
        cos_sim = map(lambda x: cosine_similarity(input_embedding, x)[0][0], doc_vec)
        scores = list(cos_sim)
        recommendations = get_recommendations(data.N, scores)
        # Return as JSON
        return recommendations.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get('/')
def hello_world():
    return {'Hello, World!'}