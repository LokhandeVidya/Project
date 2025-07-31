import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

date_range = pd.date_range(start='2025-06-01', periods=24*60, freq='H')
consumption = np.random.normal(loc=1.5, scale=0.3, size=len(date_range))

df = pd.DataFrame({
    'timestamp': date_range,
    'consumption_kWh': np.round(consumption, 2)
})

df.to_csv("data/synthetic_energy.csv", index=False)
print("✅ Data saved to data/synthetic_energy.csv")
