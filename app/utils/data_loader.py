import pandas as pd

def load_data(path="data/raw/synthetic_energy.csv"):
    return pd.read_csv(path, parse_dates=["timestamp"])
