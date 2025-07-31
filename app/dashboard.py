import streamlit as st
import pandas as pd

df = pd.read_csv("data/synthetic_energy.csv", parse_dates=["timestamp"])
df.set_index("timestamp", inplace=True)

st.header("📊 Energy Consumption Dashboard")
st.line_chart(df["consumption_kWh"])
