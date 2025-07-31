import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

df = pd.read_csv("data/processed/feature_data.csv")

X = df[["hour", "day_of_week"]]
y = df["consumption_kWh"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/energy_forecast_model.pkl")
print("✅ Model saved to models/energy_forecast_model.pkl")
