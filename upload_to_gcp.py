from google.cloud import storage
import json
from config import GCP_BUCKET_NAME

def upload_file_to_gcp(bucket_name, local_filename, gcs_filename):
    try:
        # Initialize the storage client
        client = storage.Client()  
        
        # Get the bucket
        bucket = client.bucket(bucket_name)
        
        # Create a new blob and upload the file
        blob = bucket.blob(gcs_filename)
        blob.upload_from_filename(local_filename)
        
        print(f"Successfully uploaded '{local_filename}' to 'gs://{bucket_name}/{gcs_filename}'")
    except Exception as e:
        print(f"Error uploading file to GCP: {e}")

# Example usage
if __name__ == "__main__":
    upload_file_to_gcp(GCP_BUCKET_NAME, "local_file.txt", "uploaded_file.txt")