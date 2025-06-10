
# 🍽️ Rasavilaas ML

**Rasavilaas ML** is a modern machine learning project designed to deliver intelligent ingredient-based food recommendations. Leveraging the richness of Indian cuisine, the system combines NLP techniques with similarity-based learning to create a contextual and scalable recommendation engine. The project integrates a FastAPI backend and Jupyter-based exploratory workflows, making it suitable for both experimentation and deployment.

---

## ✨ Features

- Ingredient-aware food recommendation engine
- Interactive Jupyter notebook for NLP and model training (`rasavilaas_ml.ipynb`)
- Production-ready FastAPI backend (`app.py`) to serve predictions
- Reproducible virtual environment setup (Windows/macOS/Linux)
- Clean project structure with modular codebase

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/bandishachowdhury07/Rasavilas-ML
cd Rasavilas-ML
```

### 2. Set Up the Python Virtual Environment

> Choose the commands based on your operating system.

#### Windows
```bash
python -m venv venv
source venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

To **deactivate**:
```bash
deactivate
```

To **delete** the environment:
- **macOS/Linux:** `rmdir /s /q venv`
- **Windows:** `rm -rf venv`

---

### 3. Install Dependencies

Install all necessary packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 4. Launch the Jupyter Notebook

The core data science workflow is in:

- `rasavilaas_ml.ipynb`

To configure the Jupyter kernel:
```bash
python -m ipykernel install --user --name=rasavilas_ml_env --display-name="Python (rasavilas_ml_env 3.12.10)"
jupyter notebook
```

Then select the custom kernel for execution.

---

### 5. Run the FastAPI Backend

Deploy the recommendation engine with FastAPI and Uvicorn:

```bash
uvicorn app:app --reload
```

Visit: [http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)

---

### 6. Make Predictions via API

Send a `POST` request to `/predict` with your ingredients:

**Example 1:**
```json
{
  "ingredients": "rice, egg"
}
```

**Example 2:**
```json
{
  "ingredients": "rice, egg",
  "N": 5,
  "mean": false
}
```

Test with:
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"ingredients": "rice, egg"}'
```

---

## 📁 Project Structure

| File/Folder           | Purpose                                       |
|-----------------------|-----------------------------------------------|
| `rasavilaas_ml.ipynb` | Main notebook for ML and recommendation logic |
| `app.py`              | FastAPI application for serving predictions   |
| `venv/`               | Virtual environment folder                    |
| `requirements.txt`    | List of required Python packages              |

---

## ✨ How It Works: Recommendation Logic Summary

> For a deeper technical overview, see `rasavilaas_ml.ipynb`.

### 🌎 1. Data Ingestion
- Load pre-cleaned Indian recipe dataset with ingredients and metadata.

### 📈 2. NLP Preprocessing
- Tokenize, lowercase, and clean ingredients for vectorization.

### 📊 3. Feature Extraction
- Use **TF-IDF** and **Word2Vec** to numerically represent ingredient text.

### 🔗 4. Similarity Matching
- Compute **cosine similarity** between vectorized ingredient sets.

### 🔍 5. Prediction Engine
- Return top-N similar dishes based on input ingredients.

---

## ⚡ Troubleshooting

- **Environment not activating:** Confirm OS-specific syntax.
- **Install errors:** Run `pip install --upgrade pip` and try again.

---

## 📚 References

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Jupyter Notebooks](https://jupyter.org/documentation)
- [Uvicorn](https://www.uvicorn.org/)

---

## 👉 License

MIT License

Copyright (c) 2025 Bandisha Chowdhury

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
