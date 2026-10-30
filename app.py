import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.joblib")


def category(aqi):
    if aqi <= 50:
        return "Good", "Air is fine. Enjoy outdoor activities."
    if aqi <= 100:
        return "Satisfactory", "Fine for most people. Very sensitive people should take care."
    if aqi <= 200:
        return "Moderate", "People with asthma or heart issues should limit outdoor exertion."
    if aqi <= 300:
        return "Poor", "Avoid heavy outdoor exercise. Consider a mask outdoors."
    if aqi <= 400:
        return "Very Poor", "Stay indoors where possible. No outdoor sports."
    return "Severe", "Health emergency conditions. Stay indoors."


st.title("Bengaluru AQI Predictor")
st.write("Predict tomorrow's air quality in Bengaluru from today's readings. "
         "You can find today's readings for your area on aqi.in or the CPCB website.")

today = st.number_input(
    "Today's AQI", 0, 500, 100,
    help="The main air quality number (0 to 500). Lower is better.")
pm25 = st.number_input(
    "Today's PM2.5 (µg/m³)", 0.0, 500.0, 40.0,
    help="Very fine particles from vehicles, smoke and burning. Usually listed just below the AQI.")
pm10 = st.number_input(
    "Today's PM10 (µg/m³)", 0.0, 600.0, 80.0,
    help="Coarser particles such as road and construction dust. Usually listed next to PM2.5.")

if st.button("Predict tomorrow's AQI"):
    X = pd.DataFrame([[today, pm25, pm10]], columns=["AQI", "PM2.5", "PM10"])
    pred = max(0.0, min(500.0, float(model.predict(X)[0])))
    cat, advice = category(pred)
    st.metric("Predicted AQI for tomorrow", f"{pred:.0f}")
    st.subheader(cat)
    st.info(advice)

st.caption("Educational project. Trained on 2015-2020 CPCB data for Bengaluru. "
           "Not a substitute for official CPCB advisories.")