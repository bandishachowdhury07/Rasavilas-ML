# Rasavilaas ML

Rasavilaas ML is a machine learning project designed to generate intelligent food recommendations and make ingredient-based predictions. It features a well-structured workflow using Python, Jupyter notebooks, and a FastAPI backend for serving machine learning models. This repository is suitable for both experimentation and production deployment.

---

## Features

- Ingredient-based food prediction API
- Jupyter notebook for interactive data science and ML workflows (`rasavilaas_ml.ipynb`)
- FastAPI backend (`app.py`) for serving predictions
- Easily reproducible Python virtual environment setup
- Platform-specific setup instructions (Windows, macOS, Linux)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <REPO_URL>
cd <REPO_NAME>
```

### 2. Set Up the Python Virtual Environment

> **Choose the commands based on your OS.**

#### **Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

#### **macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

To **deactivate** the virtual environment (all platforms):
```bash
deactivate
```

To **delete** the virtual environment:

- **Windows:**
  ```bash
  rmdir /s /q venv
  ```
- **macOS/Linux:**
  ```bash
  rm -rf venv
  ```

---

### 3. Install Dependencies

After activating your virtual environment, install the required packages:

```bash
pip install -r requirements.txt
```

---

### 4. Running the Jupyter Notebook

The main notebook for exploration and model development is:

- `rasavilaas_ml.ipynb`

#### **Installing a Custom Kernel**

After activating your environment, run:

```bash
python -m ipykernel install --user --name=rasavilas_ml_env --display-name="Python (rasavilas_ml_env 3.12.10)"
```

Now start Jupyter Notebook:

```bash
jupyter notebook
```

Select the kernel named **Python (rasavilas_ml_env 3.12.10)** when running the notebook.

---

### 5. Running the FastAPI Server

Serve your ML model using FastAPI and Uvicorn:

```bash
uvicorn app:app --reload
```

- By default, the API will be available at: [http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)

---

### 6. Making Predictions via API

Send POST requests to `/predict` with appropriate JSON:

**Example 1:**
```json
{
  "ingredients": "rice, egg"
}
```

**Example 2 (with additional parameters):**
```json
{
  "ingredients": "rice, egg",
  "N": 5,
  "mean": false
}
```

Use tools like [Postman](https://www.postman.com/), [httpie](https://httpie.io/), or cURL:

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"ingredients\": \"rice, egg\"}"
```

---

## Project Structure

| File/Folder         | Description                                    |
|---------------------|------------------------------------------------|
| `rasavilaas_ml.ipynb` | Main Jupyter notebook for ML exploration    |
| `app.py`            | FastAPI backend serving predictions            |
| `venv/`             | Python virtual environment directory           |
| `requirements.txt`  | Python dependencies                            |

---

## Troubleshooting

- **Virtual environment not activating:**  
  Ensure you are using the correct command for your OS and Python version.
- **Dependencies not installing:**  
  Upgrade pip with `pip install --upgrade pip` and try again.

---

## License

This project is licensed under the MIT License.

---

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Jupyter Documentation](https://jupyter.org/documentation)
- [Uvicorn](https://www.uvicorn.org/)
