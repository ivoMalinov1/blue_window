import os
from google.cloud import storage
import os
from google.cloud import texttospeech_v1
from google.cloud import storage

credentials_path = "C:\\Users\\ivoma\\BlueWindowsAssess\\blissful-canyon-391010-7b70cb6300a0.json"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path


def create_bucket(bucket_name):
    """Creates a new bucket."""
    # Try to read the GOOGLE_APPLICATION_CREDENTIALS environment variable
    credentials_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

    if credentials_path is None:
        print("The GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")
        return
    else:
        print(f"Using service account file: {credentials_path}")

    # Initialize a Cloud Storage client.
    storage_client = storage.Client.from_service_account_json(credentials_path)

    # Create the new bucket
    bucket = storage_client.bucket(bucket_name)
    new_bucket = storage_client.create_bucket(bucket)

    print(f"Bucket {new_bucket.name} created.")


# Replace 'your-bucket-name' with your desired bucket name.
create_bucket('blue-window-bucket')
