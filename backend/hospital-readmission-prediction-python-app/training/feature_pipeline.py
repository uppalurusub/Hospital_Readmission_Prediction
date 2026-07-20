import re
import joblib
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# ---------------------------------------------------------
# TEXT CLEANING
# ---------------------------------------------------------

def clean_text(text: str) -> str:

    if pd.isna(text):
        return ""

    text = text.lower()

    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


# ---------------------------------------------------------
# FEATURE ENGINEERING
# ---------------------------------------------------------

def create_engineered_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # Admission Risk Score
    df["admission_risk_score"] = (
        df["previous_admissions"] * 2
        + df["length_of_stay"]
    )

    # Medication Complexity
    df["medication_complexity"] = (
        df["medications"] / (df["length_of_stay"] + 1)
    )

    # Chronic Condition Flag
    chronic_conditions = [
        "diabetes",
        "hypertension",
        "kidney disease",
        "heart failure",
        "copd"
    ]

    df["chronic_condition_flag"] = df["diagnosis"].apply(
        lambda x: 1
        if str(x).lower() in chronic_conditions
        else 0
    )

    # High Lab Risk
    df["high_lab_risk"] = df["lab_result"].apply(
        lambda x: 1 if x > 180 else 0
    )

    # Elderly Risk
    df["elderly_risk"] = df["age"].apply(
        lambda x: 1 if x >= 65 else 0
    )

    return df


# ---------------------------------------------------------
# NUMERIC + CATEGORICAL PIPELINE
# ---------------------------------------------------------

def build_structured_pipeline():

    numeric_features = [
        "age",
        "medications",
        "lab_result",
        "previous_admissions",
        "length_of_stay",
        "admission_risk_score",
        "medication_complexity"
    ]

    categorical_features = [
        "diagnosis",
        "chronic_condition_flag",
        "high_lab_risk",
        "elderly_risk"
    ]

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features)
        ]
    )

    return preprocessor


# ---------------------------------------------------------
# TF-IDF TEXT PIPELINE
# ---------------------------------------------------------

def build_text_vectorizer():

    vectorizer = TfidfVectorizer(
        max_features=300,
        stop_words="english",
        ngram_range=(1, 2)
    )

    return vectorizer


# ---------------------------------------------------------
# COMPLETE FEATURE PIPELINE
# ---------------------------------------------------------

def prepare_features(df: pd.DataFrame):

    df = create_engineered_features(df)

    # Clean discharge summaries
    df["clean_text"] = df["discharge_summary"].apply(clean_text)

    # Structured Pipeline
    structured_pipeline = build_structured_pipeline()

    structured_features = structured_pipeline.fit_transform(df)

    # TF-IDF Features
    tfidf_vectorizer = build_text_vectorizer()

    text_features = tfidf_vectorizer.fit_transform(
        df["clean_text"]
    )

    # Combine Features
    final_features = np.hstack([
        structured_features.toarray()
        if hasattr(structured_features, "toarray")
        else structured_features,
        text_features.toarray()
    ])

    # Save preprocessors
    joblib.dump(
        structured_pipeline,
        "training/model/structured_pipeline.pkl"
    )

    joblib.dump(
        tfidf_vectorizer,
        "training/model/tfidf.pkl"
    )

    return final_features


# ---------------------------------------------------------
# INFERENCE PIPELINE
# ---------------------------------------------------------

def transform_inference_data(df: pd.DataFrame):

    df = create_engineered_features(df)

    df["clean_text"] = df["discharge_summary"].apply(clean_text)

    structured_pipeline = joblib.load(
        "training/model/structured_pipeline.pkl"
    )

    tfidf_vectorizer = joblib.load(
        "training/model/tfidf.pkl"
    )

    structured_features = structured_pipeline.transform(df)

    text_features = tfidf_vectorizer.transform(
        df["clean_text"]
    )

    final_features = np.hstack([
        structured_features.toarray()
        if hasattr(structured_features, "toarray")
        else structured_features,
        text_features.toarray()
    ])

    return final_features