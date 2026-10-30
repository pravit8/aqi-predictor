# Bengaluru AQI Predictor

A machine learning web app that forecasts tomorrow's AQI in Bengaluru from today's readings.

- Data: Air Quality Data in India (2015-2020), Kaggle, compiled from CPCB data
-- Model: Linear Regression using three inputs (today's AQI, PM2.5, PM10); MAE about 7.4 AQI points vs 8.4 for a naive baseline
- Tested simpler versions: using AQI alone made predictions worse than a naive guess, so PM2.5 and PM10 were kept, and the app explains them in plain language.
- Built with Python, pandas, scikit-learn and Streamlit

Limitations: trained on 2015-2020 data for one city; it under-predicts sudden spikes.
Educational project, not a substitute for official CPCB advisories.