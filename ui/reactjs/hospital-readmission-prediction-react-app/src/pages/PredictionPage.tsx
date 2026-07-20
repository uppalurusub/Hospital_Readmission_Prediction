import "../styles/PredictionPage.css";
import PredictionForm from "../components/PredictionForm";

export default function PredictionPage() {
  return (
    <div className="prediction-page">
      <div className="prediction-container">
        <h1 className="page-title">Hospital Readmission Prediction</h1>

        <p className="page-subtitle">
          Predict the likelihood of patient readmission using AI/ML.
        </p>

        <PredictionForm />
      </div>
    </div>
  );
}