import firebase_admin
from firebase_admin import credentials, storage

# Replace 'path/to/your/key.json' with the actual path to your service account key file
cred = credentials.Certificate('path/to/your/key.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'your-storage-bucket-name.appspot.com'
})

bucket = storage.bucket()

blob = bucket.blob('path/to/your/file.txt')  # Replace with the desired file path
blob.upload_from_filename('local/path/to/file.txt')  # Replace with the local file path
