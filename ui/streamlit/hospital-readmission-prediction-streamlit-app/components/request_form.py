import streamlit as st
def request_form():
    st.subheader("Patient Information")
    c1,c2=st.columns(2)
    with c1:
        age=st.number_input("Age",1,120,65)
        diagnosis=st.selectbox("Diagnosis",["Diabetes","Hypertension","Kidney Disease","Heart Failure","COPD","Asthma","Pneumonia","Stroke","Cancer","Liver Disease"])
        medications=st.number_input("Number of Medications",0,50,5)
    with c2:
        lab_result=st.number_input("Lab Result",0.0,500.0,150.0)
        previous_admissions=st.number_input("Previous Admissions",0,20,1)
        length_of_stay=st.number_input("Length of Stay",1,60,5)
    discharge_summary=st.text_area("Discharge Summary",height=180)
    return {"age":age,"diagnosis":diagnosis,"medications":medications,"lab_result":lab_result,"previous_admissions":previous_admissions,"length_of_stay":length_of_stay,"discharge_summary":discharge_summary}
