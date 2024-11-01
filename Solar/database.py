from pymongo import MongoClient
from config import Config
uri="mongodb://localhost:27017"
client = MongoClient(uri)
db = client['solar']


