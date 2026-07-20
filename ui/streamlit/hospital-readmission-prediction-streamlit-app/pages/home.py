import streamlit as st
from components.sidebar import show_sidebar
from components.request_form import request_form
from components.response_view import show_prediction
from api.api_client import predict

def show_home():
    st.title("🏥 Hospital Readmission Prediction")
    st.markdown("Predict whether a patient may be readmitted within 30 days using Machine Learning + NLP.")
    show_sidebar()
    payload=request_form()
    if st.button("Predict Readmission Risk"):
        show_prediction(predict(payload),payload)
