import os
from pymongo import MongoClient

# Fetch the MongoDB URI from environment variables
uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')  # Default to local if not set
client = MongoClient(uri)

# Specify your database
db = client['solar']
