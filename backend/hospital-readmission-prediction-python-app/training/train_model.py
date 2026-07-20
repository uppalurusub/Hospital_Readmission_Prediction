import joblib
import mlflow
import mlflow.lightgbm
import lightgbm as lgb
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from training.feature_pipeline import (
    transform_inference_data
)

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

df = pd.read_csv("../data/readmission.csv")

# ---------------------------------------------------------
# TARGET
# ---------------------------------------------------------

TARGET_COLUMN = "target"

X = df.drop(TARGET_COLUMN, axis=1)

y = df[TARGET_COLUMN]

# ---------------------------------------------------------
# FEATURE ENGINEERING + NLP
# ---------------------------------------------------------

X_features = transform_inference_data(X)

# ---------------------------------------------------------
# TRAIN TEST SPLIT
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_features,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------------------------
# MODEL
# ---------------------------------------------------------

model = lgb.LGBMClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6
)

# ---------------------------------------------------------
# MLFLOW
# ---------------------------------------------------------

mlflow.set_experiment(
    "Hospital_Readmission_Prediction"
)

with mlflow.start_run():

    # Train
    model.fit(X_train, y_train)

    # Predict
    preds = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, preds)

    print(f"Accuracy: {accuracy}")

    # Log metrics
    mlflow.log_metric("accuracy", accuracy)

    # Log parameters
    mlflow.log_param("n_estimators", 200)
    mlflow.log_param("learning_rate", 0.05)
    mlflow.log_param("max_depth", 6)

    # Save model
    joblib.dump(
        model,
        "training/model/lightgbm_model.pkl"
    )

    # Log model
    mlflow.lightgbm.log_model(
        model,
        artifact_path="model"
    )

print("Training completed successfully.")