import streamlit as st
from utils.formatters import patient_dataframe
def show_prediction(result,payload):
    if "error" in result:
        st.error(result["error"]);return
    c1,c2,c3=st.columns(3)
    c1.metric("Prediction",result["prediction"])
    c2.metric("Probability",f'{result["probability"]*100:.2f}%')
    c3.metric("Risk Level",result["risk_level"])
    df=patient_dataframe(payload)
    st.dataframe(df,use_container_width=True)
    st.bar_chart(df.set_index("Feature"))
