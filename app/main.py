import streamlit as st
import pandas as pd
import joblib

# Load data and model
df = pd.read_csv("data/synthetic_energy.csv", parse_dates=["timestamp"])
model = joblib.load("model/model.pkl")

# Feature engineering
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day
df["weekday"] = df["timestamp"].dt.weekday
df["is_weekend"] = df["weekday"] >= 5

# Predict
X = df[["hour", "day", "weekday", "is_weekend"]]
df["prediction"] = model.predict(X)

# Streamlit app
st.title("🔋 Residential Energy Analytics")
st.write("Track and forecast household energy usage.")

st.line_chart(df.set_index("timestamp")[["consumption_kWh", "prediction"]])

