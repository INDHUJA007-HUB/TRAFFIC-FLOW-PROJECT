# Configuration file for Traffic Flow Visualization project

# Google Cloud Storage settings
GCP_BUCKET_NAME = "your-traffic-data-bucket"
GCP_PROJECT_ID = "your-gcp-project-id"

# API settings (Replace with actual API keys or URLs)
TRAFFIC_API_URL = "https://traffic-data-api.example.com"
TRAFFIC_API_KEY = "your-api-key"

# Streamlit App settings
APP_TITLE = "Real-Time Traffic Flow Visualization"
MAPBOX_ACCESS_TOKEN = "your-mapbox-token"

# Database settings (Optional)
DATABASE_HOST = "localhost"
DATABASE_USER = "your-db-user"
DATABASE_PASSWORD = "your-db-password"
DATABASE_NAME = "traffic_db"

# Logging settings
LOG_FILE = "traffic_app.log"
DEBUG_MODE = True  # Set to False in production

# Other project-specific settings
DATA_REFRESH_INTERVAL = 300  # Time in seconds (e.g., update every 5 minutes)
