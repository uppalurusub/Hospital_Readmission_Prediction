# 🏥 Hospital Readmission Prediction - React + TypeScript Frontend

A modern React + TypeScript web application for predicting the likelihood of hospital patient readmission using a Machine Learning model exposed through a REST API.

The application provides an intuitive interface for entering patient clinical information, sending prediction requests to a FastAPI backend, and displaying AI-generated prediction results including probability and risk level.

---

# Features

- Modern React 18 + TypeScript application
- Clean responsive UI
- Patient information form
- REST API integration using Axios
- Prediction Result dashboard
- Risk Level visualization
- Probability display
- Component-based architecture
- Easy integration with FastAPI backend
- Vite build system for lightning-fast development

---

# Technology Stack

| Technology | Version |
|------------|----------|
| React | 18+ |
| TypeScript | 5+ |
| Vite | Latest |
| Axios | Latest |
| CSS3 | Custom Styling |

---

# Project Structure

```
src/
│
├── api/
│   ├── apiClient.ts
│   └── predictionApi.ts
│
├── assets/
│   ├── hero.png
│   ├── react.svg
│   └── vite.svg
│
├── components/
│   ├── PredictionForm.tsx
│   └── PredictionResult.tsx
│
├── models/
│   ├── PredictionRequest.ts
│   └── PredictionResponse.ts
│
├── pages/
│   └── PredictionPage.tsx
│
├── styles/
│   ├── PredictionForm.css
│   └── PredictionPage.css
│
├── App.tsx
├── App.css
├── main.tsx
└── index.css
```

---

# Application Workflow

```
User

   │

   ▼

Prediction Form

   │

   ▼

Axios API Client

   │

   ▼

FastAPI Backend

   │

   ▼

Machine Learning Model

   │

   ▼

Prediction Response

   │

   ▼

Prediction Result Dashboard
```

---

# Prediction Request

The application sends the following JSON request:

```json
{
  "age": 71,
  "diagnosis": "Diabetes",
  "medications": 9,
  "lab_result": 220,
  "previous_admissions": 4,
  "length_of_stay": 7,
  "discharge_summary": "Patient discharged with unstable blood sugar and renal complications."
}
```

---

# Prediction Response

```json
{
  "prediction": "Readmitted",
  "probability": 0.87,
  "risk_level": "High"
}
```

---

# API Configuration

Current backend configuration:

```typescript
http://localhost:8000
```

Prediction Endpoint

```
POST /predict/
```

Configured in

```
src/api/apiClient.ts
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-org/hospital-readmission-ui.git
```

Navigate to project

```bash
cd hospital-readmission-ui
```

Install dependencies

```bash
npm install
```

Run development server

```bash
npm run dev
```

Application runs at

```
http://localhost:5173
```

---

# Build Production

```bash
npm run build
```

Preview production build

```bash
npm run preview
```

---

# Components

## PredictionPage

Responsibilities

- Main application page
- Displays title
- Displays subtitle
- Loads PredictionForm

---

## PredictionForm

Responsibilities

- Collect patient information
- Manage form state
- Call backend API
- Handle loading state
- Display prediction results

Patient Inputs

- Age
- Diagnosis
- Number of Medications
- Lab Result
- Previous Admissions
- Length of Stay
- Discharge Summary

---

## PredictionResult

Displays

- Prediction
- Prediction Probability
- Risk Level

---

# Data Models

## PredictionRequest

```typescript
interface PredictionRequest {
    age: number;
    diagnosis: string;
    medications: number;
    lab_result: number;
    previous_admissions: number;
    length_of_stay: number;
    discharge_summary: string;
}
```

---

## PredictionResponse

```typescript
interface PredictionResponse {
    prediction: string;
    probability: number;
    risk_level: string;
}
```

---

# API Layer

## apiClient.ts

Responsible for

- Axios configuration
- Base URL
- Shared HTTP client

---

## predictionApi.ts

Responsible for

- Calling prediction endpoint
- Returning typed response

---

# Current Features

- Patient Readmission Prediction
- REST API Communication
- Strong TypeScript Models
- Loading State Handling
- Responsive UI
- Modular Architecture

---

# Future Enhancements

- Authentication
- JWT Security
- Form Validation
- Error Boundary
- Toast Notifications
- Prediction History
- Charts & Analytics
- Export Prediction Report (PDF)
- Dark Theme
- Multi-language Support
- Environment-based API URLs
- Docker Support
- Kubernetes Deployment
- Azure App Service Deployment

---

# Recommended Environment Variables

Create

```
.env
```

```env
VITE_API_BASE_URL=http://localhost:8000
```

Update

```typescript
const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL
});
```

---

# Scripts

```bash
npm install
```

Install dependencies

```bash
npm run dev
```

Run development server

```bash
npm run build
```

Create production build

```bash
npm run preview
```

Preview production build

---

# Backend Requirements

The frontend expects a FastAPI backend exposing:

```
POST /predict/
```

Response

```json
{
    "prediction": "Readmitted",
    "probability": 0.87,
    "risk_level": "High"
}
```

---

# Screens

- Hospital Readmission Prediction Dashboard
- Patient Information Form
- Prediction Result Card
- Probability Indicator
- Risk Level Badge

---

# Best Practices Used

- Functional Components
- TypeScript Interfaces
- Component Separation
- API Abstraction Layer
- Modular Folder Structure
- Strong Typing
- Reusable Components
- CSS Separation
- Clean Architecture

---

# License

This project is intended for educational, research, and healthcare AI demonstration purposes.

---

# Author

Hospital Readmission Prediction Frontend

React + TypeScript + Vite

Integrated with FastAPI Machine Learning Backend.