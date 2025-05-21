import pandas as pd
import random
from datetime import datetime

def get_traffic_data():
    data = {
        "latitude": [random.uniform(40.60, 40.80) for _ in range(100)],
        "longitude": [random.uniform(-74.10, -73.90) for _ in range(100)],
        "vehicle_count": [random.randint(5, 50) for _ in range(100)],
        "speed": [random.uniform(20, 80) for _ in range(100)],
        "timestamp": [datetime.utcnow().isoformat()] * 100
    }
    df = pd.DataFrame(data)
    df.to_csv("traffic_data.csv", index=False)
    return df
