import pandas as pd
import numpy as np
import os

os.makedirs("data/raw", exist_ok=True)

date_range = pd.date_range(start='2025-01-01', periods=24*30, freq='H')
consumption = np.random.normal(loc=1.5, scale=0.5, size=len(date_range))

df = pd.DataFrame({
    'timestamp': date_range,
    'consumption_kWh': np.clip(np.round(consumption, 2),0,None)
})

df.to_csv("data/raw/synthetic_energy.csv", index=False)
print("✅data/raw/synthetic_energy.csv generated")
