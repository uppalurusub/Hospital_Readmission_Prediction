import joblib
import pandas as pd

from training.feature_pipeline import (
    transform_inference_data
)

# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------

model = joblib.load(
    "training/model/lightgbm_model.pkl"
)

# ---------------------------------------------------------
# PREDICTION FUNCTION
# ---------------------------------------------------------

def predict_model(data):

    # Convert request to dataframe
    input_df = pd.DataFrame([{
        "patient_id": "TEMP001",
        "age": data.age,
        "diagnosis": data.diagnosis,
        "medications": data.medications,
        "lab_result": data.lab_result,
        "previous_admissions": data.previous_admissions,
        "length_of_stay": data.length_of_stay,
        "discharge_summary": data.discharge_summary
    }])

    # Use SAME TRAINING PIPELINE
    final_features = transform_inference_data(
        input_df
    )

    # Prediction
    prediction = model.predict(final_features)[0]

    probability = model.predict_proba(
        final_features
    )[0][1]

    # Risk Level
    if probability > 0.7:
        risk_level = "HIGH"

    elif probability > 0.4:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return {
        "prediction": (
            "READMITTED"
            if prediction == 1
            else "NOT_READMITTED"
        ),
        "probability": round(float(probability), 2),
        "risk_level": risk_level
    }