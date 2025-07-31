import streamlit as st
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from app.utils.model_utils import load_model

def show_forecast():
    st.title("🔮 Forecast Energy Consumption")

    model = load_model()
    hour = st.slider("Hour", 0, 23)
    day = st.slider("Day of Week (0=Mon)", 0, 6)

    prediction = model.predict([[hour, day]])[0]
    st.metric("🔮 Forecasted Consumption", f"{prediction:.2f} kWh")

show_forecast()

