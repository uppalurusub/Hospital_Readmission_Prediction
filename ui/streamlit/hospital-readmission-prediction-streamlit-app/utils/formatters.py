import pandas as pd
def patient_dataframe(p):
    return pd.DataFrame({"Feature":["Age","Medications","Lab Result","Previous Admissions","Length of Stay"],"Value":[p["age"],p["medications"],p["lab_result"],p["previous_admissions"],p["length_of_stay"]]})
