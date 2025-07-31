import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

# Load data
df = pd.read_csv("data/synthetic_energy.csv", parse_dates=["timestamp"])
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day
df["weekday"] = df["timestamp"].dt.weekday
df["is_weekend"] = df["weekday"] >= 5

# Features and target
X = df[["hour", "day", "weekday", "is_weekend"]]
y = df["consumption_kWh"]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")
print("✅ Model trained and saved to model/model.pkl")

