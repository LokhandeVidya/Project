# main.py

import streamlit as st
import pandas as pd
import joblib
import os
from utils.helpers import extract_features

st.title("🏠 Residential Energy Forecasting")

uploaded_file = st.file_uploader("Upload your CSV file with timestamps")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=["timestamp"])
    st.write("📄 Input Data Preview", df.head())

    # Save uploaded file so dashboard can access it
    save_path = os.path.join("data", "raw", "synthetic_energy.csv")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)

    # Feature Engineering
    df = extract_features(df)

    # Load model
    model = joblib.load("models/energy_forecast_model.pkl")

    # Predict
    df["predicted_energy"] = model.predict(df[["hour", "day_of_week"]])

    st.write("⚡ Forecasted Energy Consumption", df[["timestamp", "predicted_energy"]])
