import requests
import pandas as pd
from config import TRAFFIC_API_URL

def get_traffic_data():
    try:
        response = requests.get(TRAFFIC_API_URL)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            print(f"Error fetching data: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return None