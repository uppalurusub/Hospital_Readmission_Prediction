# 🏥 Hospital Readmission Prediction System

> An End-to-End Machine Learning Project for Predicting Hospital Readmission using Structured Clinical Data and NLP

---

# 📌 Overview

Hospital readmission is one of the most important quality indicators in healthcare. Predicting patients who are at high risk of being readmitted enables hospitals to:

- Improve patient outcomes
- Reduce healthcare costs
- Optimize discharge planning
- Reduce preventable readmissions
- Improve operational efficiency

This project provides a complete production-ready machine learning solution for predicting hospital readmission using both structured patient information and unstructured discharge summaries.

The project includes:

- Machine Learning Model
- NLP Feature Engineering
- FastAPI REST API
- Streamlit Web Application
- MLflow Experiment Tracking
- Docker Deployment
- Modular Python Architecture

---

# 🚀 Project Features

## Machine Learning

- LightGBM Classification Model
- Structured Clinical Feature Engineering
- Prediction Probability
- Model Serialization
- Production Inference Pipeline

---

## Natural Language Processing

The project extracts useful information from discharge summaries using TF-IDF.

Example:

```
Discharge Summary
        ↓
Text Cleaning
        ↓
TF-IDF Vectorization
        ↓
Feature Matrix
        ↓
LightGBM Model
```

---

## API

REST API built using FastAPI.

Features include:

- JSON Request Validation
- Prediction Endpoint
- Swagger Documentation
- Error Handling
- Pydantic Models

---

## Streamlit UI

Interactive prediction interface with:

- Patient Information Form
- Real-time Predictions
- Probability Display
- Clean Dashboard

---

## MLflow

Tracks

- Experiments
- Parameters
- Metrics
- Models
- Artifacts

---

## Docker Support

Project includes

- Dockerfile for API
- Dockerfile for Streamlit
- Docker Compose



# 🧠 Machine Learning Pipeline

```
Patient Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
NLP Processing
        │
        ▼
TF-IDF
        │
        ▼
Train/Test Split
        │
        ▼
LightGBM Model
        │
        ▼
Evaluation
        │
        ▼
MLflow Logging
        │
        ▼
Model Serialization
        │
        ▼
FastAPI Prediction Service
```

---

# 📊 Dataset

The dataset contains patient clinical information including:

| Feature | Description |
|----------|-------------|
| Age | Patient Age |
| Diagnosis | Disease Description |
| Medications | Number of Medications |
| Lab Result | Laboratory Score |
| Previous Admissions | Historical Admissions |
| Length of Stay | Hospital Stay |
| Discharge Summary | Clinical Notes |
| Target | Readmission (0/1) |

---

# ⚙️ Technologies Used

| Category | Technology |
|-----------|------------|
| Language | Python |
| Machine Learning | LightGBM |
| NLP | TF-IDF |
| API | FastAPI |
| Validation | Pydantic |
| Tracking | MLflow |
| UI | Streamlit |
| Deployment | Docker |
| Data | Pandas |
| ML | Scikit-Learn |

---

# 📈 Model

Current model:

- LightGBM Classifier

Target Variable

```
target

0 → No Readmission

1 → Readmission
```

---

# 📊 Evaluation Metrics

The project generates:

- Accuracy
- Precision
- Recall
- F1 Score
- Classification Report
- ROC Curve
- Feature Importance

Reports are stored inside:

```
reports/
```

---

# 🚀 Running Model Training

```
python training/train_model.py
```

The script will:

- Load dataset
- Perform feature engineering
- Build NLP features
- Train LightGBM
- Evaluate model
- Save model
- Log experiment to MLflow

---

# 📈 MLflow

Start MLflow

```
mlflow ui
```

Default URL

```
http://localhost:5000
```

Tracked Items

- Parameters
- Accuracy
- Model
- Artifacts

---

# 🚀 Running FastAPI

```
uvicorn app.main:app --reload
```

API URL

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# Example Request

```json
{
    "age": 65,
    "diagnosis": "Diabetes",
    "medications": 5,
    "lab_result": 89.5,
    "previous_admissions": 2,
    "length_of_stay": 7,
    "discharge_summary": "Patient discharged in stable condition with insulin therapy."
}
```

---

# Example Response

```json
{
    "prediction": 1,
    "probability": 0.91,
    "message": "High Risk of Readmission"
}
```

---

# 🖥 Streamlit

Run

```
streamlit run streamlit_app.py
```

Features

- Patient Input Form
- Prediction
- Probability
- Interactive Dashboard

---

# 🐳 Docker

Build API

```
docker build -f Dockerfile.api -t hospital-api .
```

Run

```
docker-compose up
```

---

# 📁 Saved Models

```
training/model/

lightgbm_model.pkl
structured_pipeline.pkl
tfidf.pkl
```

---

# Feature Engineering

Structured Features

- Age
- Previous Admissions
- Length of Stay
- Lab Result
- Medications

NLP Features

- Discharge Summary
- TF-IDF Vectorization

---

# API Architecture

```
Request

   │

Router

   │

Service

   │

Implementation

   │

Prediction Model

   │

Response
```

---

# Future Enhancements

- XGBoost
- CatBoost
- Random Forest
- Explainable AI (SHAP)
- Feature Store
- Model Registry
- CI/CD Pipeline
- Kubernetes Deployment
- Azure Deployment
- Batch Prediction
- Real-time Monitoring

---

# Author

Machine Learning Project

Hospital Readmission Prediction

Built using

- Python
- LightGBM
- FastAPI
- Streamlit
- MLflow
- Docker

---