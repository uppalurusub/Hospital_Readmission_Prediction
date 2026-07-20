def create_features(df):

    df["admission_risk_score"] = (
        df["previous_admissions"] * 2
        + df["length_of_stay"]
    )

    return df