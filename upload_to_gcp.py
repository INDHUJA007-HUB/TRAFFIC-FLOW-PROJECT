from google.cloud import storage
import json
from config import GCP_BUCKET_NAME

def upload_file_to_gcp(bucket_name, local_filename, gcs_filename):
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(gcs_filename)
        blob.upload_from_filename(local_filename)
        print(f"✅ Uploaded {local_filename} to {bucket_name}/{gcs_filename}")
    except Exception as e:
        print(f"❌ Error uploading file to GCP: {str(e)}")