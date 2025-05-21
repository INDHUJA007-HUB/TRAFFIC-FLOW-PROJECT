import os

# Configuration for Traffic Flow Project

# Google Cloud Storage settings
GCP_BUCKET_NAME = os.getenv("GCP_BUCKET_NAME", "your-traffic-data-bucket")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "your-gcp-project-id")

# Traffic Data API settings
TRAFFIC_API_URL = "https://your-traffic-api.com"
# TRAFFIC_API_URL = os.getenv("TRAFFIC_API_URL", "https://your-traffic-api.com")
TRAFFIC_API_KEY = os.getenv("TRAFFIC_API_KEY", "your-api-key")  # Store securely!

# Streamlit settings
APP_TITLE = "🚦 Real-Time Traffic Flow Visualization"
MAPBOX_ACCESS_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN", "your-mapbox-token")

# Logging settings
LOG_FILE = os.getenv("LOG_FILE", "traffic_app.log")
DEBUG_MODE = bool(os.getenv("DEBUG_MODE", True))  # Ensures the value is boolean

DATA_REFRESH_INTERVAL = 30  # Example value

# Debugging Output
print(f"Using GCP Bucket: {GCP_BUCKET_NAME}")
print(f"Traffic API URL: {TRAFFIC_API_URL}")
print(f"Debug Mode: {DEBUG_MODE}")
