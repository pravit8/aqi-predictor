import streamlit as st
import joblib
import pandas as pd
import datetime

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
st.write("Enter today's readings to get a forecast for tomorrow. "
         "You can find live readings on the CPCB website or on aqi.in.")

today = st.number_input("Today's AQI", 0, 500, 100)
yesterday = st.number_input("Yesterday's AQI", 0, 500, 100)
avg7 = st.number_input("Average AQI of the last 7 days", 0, 500, 100)
pm25 = st.number_input("Today's PM2.5", 0.0, 500.0, 40.0)
pm10 = st.number_input("Today's PM10", 0.0, 600.0, 80.0)

if st.button("Predict tomorrow's AQI"):
    X = pd.DataFrame(
        [[today, yesterday, avg7, pm25, pm10, datetime.date.today().month]],
        columns=["AQI", "AQI_lag1", "AQI_roll7", "PM2.5", "PM10", "month"],
    )
    pred = float(model.predict(X)[0])
    cat, advice = category(pred)
    st.metric("Predicted AQI for tomorrow", f"{pred:.0f}", cat, delta_color="off")
    st.info(advice)

st.caption("Educational project. Trained on 2015-2020 CPCB data for Bengaluru. "
           "Not a substitute for official CPCB advisories.")