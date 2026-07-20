import pandas as pd

def preprocess_input(data):

    processed = {
        "age": data.age,
        "medications": data.medications,
        "lab_result": data.lab_result,
        "previous_admissions": data.previous_admissions,
        "length_of_stay": data.length_of_stay
    }

    return pd.DataFrame([processed])