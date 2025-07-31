import joblib

def load_model(path="models/energy_forecast_model.pkl"):
    return joblib.load(path)
