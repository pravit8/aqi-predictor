# Bengaluru AQI Predictor

A machine learning web app that forecasts tomorrow's AQI in Bengaluru from today's readings.

- Data: Air Quality Data in India (2015-2020), Kaggle, compiled from CPCB data
- Model: Linear Regression (MAE about 7.4 AQI points, beating a naive baseline of 8.4)
- Built with Python, pandas, scikit-learn and Streamlit

Limitations: trained on 2015-2020 data for one city; it under-predicts sudden spikes.
Educational project, not a substitute for official CPCB advisories.