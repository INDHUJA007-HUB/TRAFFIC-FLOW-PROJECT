import requests
import pandas as pd
from config import TRAFFIC_API_URL

def get_traffic_data():
    try:
        # Define headers (if required)
        headers = {"Accept": "application/json"}
        
        # Fetch traffic data from API
        response = requests.get(TRAFFIC_API_URL, headers=headers)
        response.raise_for_status()  # Raise an error for non-200 responses
        
        # Parse JSON response
        data = response.json()
        
        # Validate JSON structure
        if isinstance(data, list) and data:  # Check if it's a non-empty list
            return pd.DataFrame(data)
        else:
            print("⚠️ Invalid response format or empty data.")
            return None
    
    except requests.exceptions.RequestException as req_err:
        print(f"🚨 API Request Failed: {req_err}")
    except ValueError:
        print("⚠️ Error decoding JSON response.")
    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")

    return None  # Ensures function returns None in case of failure