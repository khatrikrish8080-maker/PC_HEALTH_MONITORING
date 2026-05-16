import streamlit as st
import psutil
import pickle
import numpy as np


model=pickle.load(open('PC_Health_modelling.pkl','rb'))


st.title("🖥️ PC HEALTH SENTINEL")
st.subheader("Automated Hardware Diagnostics using Machine Learning")

if st.button("🔍 Start Health Analysis for my system"):
    cpu_usage=psutil.cpu_percent(interval=1)
    ram_usage=psutil.virtual_memory().percent
    battery=psutil.sensors_battery().percent

    is_plugged = 1 if psutil.sensors_battery().power_plugged else 0


    col1,col2,col3=st.columns(3)
    col1.metric("⚡ CPU Load", f"{cpu_usage}%")
    col2.metric("💾 RAM Usage", f"{ram_usage}%")
    col3.metric("🔋 Battery Level", f"{battery}%")
    

    features=np.array([[cpu_usage,ram_usage,battery,is_plugged]])

    print("FEATURES SENT TO MODEL:", features)
    print("MODEL PREDICTION OUTPUT:", model.predict(features))

    prediction=model.predict(features)[0]

    st.subheader("Diagnostic Verdict:")
        
    if prediction == 1:
            st.success("✅ SYSTEM HEALTHY: Your hardware is operating within optimal parameters.")
    elif prediction == 2:
            st.warning("⚠️ WARNING: High resource utilization detected. Close background apps.")
    elif prediction == 0:
            st.error("🚨 CRITICAL: Hardware stress detected. Potential for thermal throttling or system crash.")

with st.expander("🔍 How this Prediction Was Made"):
        st.markdown("""
        ### **Behind the Scenes:**
        * **The Brains:** This system uses a trained **Support Vector Classifier (SVC)** machine learning model.
        * **The Input Matrix:** The raw metrics ($[CPU, RAM, Battery]$) were scaled and transformed into a 2D feature vector.
        * **The Decision Boundary:** The model evaluated where this point lies relative to its learned decision boundaries across three distinct health states (**Healthy**, **Warning**, and **Critical**).
        """)
