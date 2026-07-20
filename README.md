# 🏥 Hospital Readmission Prediction System

An end-to-end Machine Learning application for predicting the likelihood of patient hospital readmission using structured clinical data and unstructured discharge summaries.

The project consists of:

- **Backend:** FastAPI + Machine Learning + NLP + MLflow
- **Frontend:** React + TypeScript + Vite
- **Model:** LightGBM Classification Pipeline
- **NLP:** TF-IDF based text feature extraction
- **Deployment Ready:** REST API with React UI

---

# Project Architecture

```
Hospital_Readmission_Prediction
│
├── backend
│   ├── hospital-readmission-prediction-python-app
│   ├── data
│   └── README.md
│
├── ui
│   └── reactjs
│       └── hospital-readmission-prediction-react-app
│
├── requirements.txt
└── README.md
```

---

# Features

## Backend

- FastAPI REST API
- Readmission prediction endpoint
- Structured feature preprocessing
- NLP processing of discharge summaries
- Feature Engineering
- LightGBM Classification Model
- MLflow integration
- Model Evaluation
- Classification Reports
- ROC Curve generation
- Feature Importance reports
- Modular project architecture
- CORS enabled for React frontend

---

## Frontend

- React 19
- TypeScript
- Vite
- Axios REST integration
- Prediction Form
- Prediction Results
- Responsive UI
- REST API communication

---

# Machine Learning Workflow

```
Clinical Data
        │
        ▼
Feature Engineering
        │
        ▼
Discharge Summary NLP
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Structured Pipeline
        │
        ▼
LightGBM Model
        │
        ▼
Readmission Prediction
```

---

# Technology Stack

## Backend

- Python
- FastAPI
- Pydantic
- LightGBM
- Scikit-Learn
- Pandas
- NumPy
- MLflow

---

## Frontend

- React
- TypeScript
- Vite
- Axios
- HTML5
- CSS3

---

# Backend Structure

```
backend
│
├── data
│
├── hospital-readmission-prediction-python-app
│
├── implementations
│     ├── feature_engineering.py
│     ├── preprocessing.py
│     ├── model_predictor.py
│     ├── mlflow_manager.py
│     └── nlp_processor.py
│
├── training
│     ├── train_model.py
│     ├── evaluate_model.py
│     ├── feature_pipeline.py
│     └── model
│
├── routers
├── services
├── models
├── reports
├── utils
└── main.py
```

---

# Frontend Structure

```
ui/reactjs
│
├── src
│   ├── api
│   ├── components
│   ├── models
│   ├── pages
│   ├── App.tsx
│   └── main.tsx
│
├── package.json
└── vite.config
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>

cd Hospital_Readmission_Prediction
```

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Backend

Navigate to:

```
backend/hospital-readmission-prediction-python-app
```

Start FastAPI

```bash
uvicorn main:app --reload
```

Backend runs on

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Frontend Setup

Navigate to

```
ui/reactjs/hospital-readmission-prediction-react-app
```

Install packages

```bash
npm install
```

Run

```bash
npm run dev
```

Application

```
http://localhost:5173
```

---

# API Endpoint

## Predict Readmission

```
POST /predict/
```

Sample Request

```json
{
  "age": 65,
  "diagnosis": "Heart Failure",
  "medications": 8,
  "lab_result": 7.8,
  "previous_admissions": 2,
  "length_of_stay": 5,
  "discharge_summary": "Patient discharged with medication adjustments and follow-up care."
}
```

Sample Response

```json
{
  "prediction": "High Risk",
  "probability": 0.91
}
```

---

# Machine Learning Pipeline

The project performs:

- Data preprocessing
- Feature engineering
- NLP text vectorization
- Structured feature transformation
- Model training
- Model evaluation
- Prediction serving
- MLflow experiment tracking

---

# Model Artifacts

Generated artifacts include:

- Trained LightGBM Model
- Structured Pipeline
- TF-IDF Vectorizer
- Classification Report
- ROC Curve
- Feature Importance Report

---

# Reports

The application generates:

- Classification Report
- ROC Curve
- Feature Importance CSV

---

# CORS Configuration

The backend is configured to allow requests from:

```
http://localhost:5173
http://127.0.0.1:5173
```

---

# Future Enhancements

- Docker support
- Kubernetes deployment
- Authentication & Authorization
- Explainable AI (SHAP/LIME)
- Batch Predictions
- Model Monitoring
- Drift Detection
- CI/CD Pipeline
- Cloud Deployment (Azure/AWS/GCP)

---

# Project Highlights

- Full Stack Machine Learning Application
- FastAPI REST API
- React TypeScript Frontend
- LightGBM Classification
- NLP Integration
- MLflow Tracking
- Modular Architecture
- Production Ready Design
- Healthcare Analytics Use Case

---

# License

This project is intended for educational, research, and healthcare analytics purposes. Customize the license according to your organization's requirements.

---

# Author

Hospital Readmission Prediction System

Developed using:

- FastAPI
- React
- TypeScript
- LightGBM
- MLflow
- Scikit-Learn
- Python