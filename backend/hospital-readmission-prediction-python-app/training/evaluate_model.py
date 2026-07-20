import json
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    roc_curve
)



from training.feature_pipeline import (
    transform_inference_data
)

# ---------------------------------------------------------
# LOAD TEST DATA
# ---------------------------------------------------------

TEST_DATA_PATH = "data/readmission_test.csv"

MODEL_PATH = "training/model/lightgbm_model.pkl"

TARGET_COLUMN = "target"

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

print("Loading test dataset...")

df = pd.read_csv(TEST_DATA_PATH)

print(f"Dataset Shape: {df.shape}")

# ---------------------------------------------------------
# SPLIT FEATURES & TARGET
# ---------------------------------------------------------

X = df.drop(TARGET_COLUMN, axis=1)

y = df[TARGET_COLUMN]

# ---------------------------------------------------------
# FEATURE TRANSFORMATION
# ---------------------------------------------------------

print("Preparing features...")

X_features = transform_inference_data(X)

# ---------------------------------------------------------
# LOAD TRAINED MODEL
# ---------------------------------------------------------

print("Loading trained model...")

model = joblib.load(MODEL_PATH)

# ---------------------------------------------------------
# PREDICTIONS
# ---------------------------------------------------------

print("Running predictions...")

y_pred = model.predict(X_features)

y_prob = model.predict_proba(X_features)[:, 1]

# ---------------------------------------------------------
# EVALUATION METRICS
# ---------------------------------------------------------

accuracy = accuracy_score(y, y_pred)

precision = precision_score(y, y_pred)

recall = recall_score(y, y_pred)

f1 = f1_score(y, y_pred)

roc_auc = roc_auc_score(y, y_prob)

# ---------------------------------------------------------
# PRINT METRICS
# ---------------------------------------------------------

print("\nModel Evaluation Metrics")
print("-" * 40)

print(f"Accuracy     : {accuracy:.4f}")
print(f"Precision    : {precision:.4f}")
print(f"Recall       : {recall:.4f}")
print(f"F1 Score     : {f1:.4f}")
print(f"ROC-AUC      : {roc_auc:.4f}")

# ---------------------------------------------------------
# CONFUSION MATRIX
# ---------------------------------------------------------

cm = confusion_matrix(y, y_pred)

print("\nConfusion Matrix")
print(cm)

# ---------------------------------------------------------
# CLASSIFICATION REPORT
# ---------------------------------------------------------

report = classification_report(
    y,
    y_pred,
    output_dict=True
)

print("\nClassification Report")
print(classification_report(y, y_pred))

# ---------------------------------------------------------
# SAVE CLASSIFICATION REPORT
# ---------------------------------------------------------

with open("reports/classification_report.json", "w") as file:
    json.dump(report, file, indent=4)

# ---------------------------------------------------------
# ROC CURVE
# ---------------------------------------------------------

fpr, tpr, thresholds = roc_curve(y, y_prob)

plt.figure(figsize=(8, 6))

plt.plot(fpr, tpr)

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.grid(True)

plt.savefig("reports/roc_curve.png")

plt.close()

# ---------------------------------------------------------
# FEATURE IMPORTANCE
# ---------------------------------------------------------

if hasattr(model, "feature_importances_"):

    importance_df = pd.DataFrame({
        "importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        by="importance",
        ascending=False
    )

    importance_df.to_csv(
        "reports/feature_importance.csv",
        index=False
    )

    print("\nFeature importance saved.")

# ---------------------------------------------------------
# MLFLOW LOGGING
# ---------------------------------------------------------

with mlflow.start_run(run_name="Model_Evaluation"):

    mlflow.log_metric("accuracy", accuracy)

    mlflow.log_metric("precision", precision)

    mlflow.log_metric("recall", recall)

    mlflow.log_metric("f1_score", f1)

    mlflow.log_metric("roc_auc", roc_auc)

    mlflow.log_artifact(
        "reports/classification_report.json"
    )

    mlflow.log_artifact(
        "reports/roc_curve.png"
    )

    if hasattr(model, "feature_importances_"):

        mlflow.log_artifact(
            "reports/feature_importance.csv"
        )

    mlflow.sklearn.log_model(
        model,
        artifact_path="evaluated_model"
    )

print("\nEvaluation completed successfully.")