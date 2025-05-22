import pandas as pd
import logging

def get_traffic_data():
    try:
        # Use absolute path
        return pd.read_csv("C:/Users/indhu/traffic_flow_project/sample_traffic_data.csv")
    except Exception as e:
        logging.error(f"Failed to load local data: {e}")
        return None

if __name__ == "__main__":
    df = get_traffic_data()
    if df is not None:
        print(df.head())
    else:
        print("Failed to load traffic data.")
