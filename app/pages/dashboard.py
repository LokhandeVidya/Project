import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Correct path based on your folder structure
CSV_PATH = os.path.join("data", "raw", "synthetic_energy.csv")

def load_data():
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    else:
        return None

def show_dashboard():
    st.title("📊 Energy Usage Dashboard")

    df = load_data()
    if df is None:
        st.warning("⚠️ Data not found. Please upload a file on the main page.")
        return

    st.subheader("📌 Summary Statistics")
    st.write(df['consumption_kWh'].describe())

    st.subheader("🔋 Energy Consumption Over Time")
    fig, ax = plt.subplots()
    ax.plot(df['timestamp'], df['consumption_kWh'], color='skyblue', label='Consumption (kWh)')
    ax.set_xlabel("Time")
    ax.set_ylabel("kWh")
    ax.legend()
    st.pyplot(fig)

show_dashboard()
