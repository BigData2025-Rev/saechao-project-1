import logging
import os
from pymongo import MongoClient
from dotenv import load_dotenv



# Load DB envirement variable
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME= os.getenv("DB_NAME")

client = MongoClient(f"mongodb://{DB_HOST}:{DB_PORT}/")


# client = MongoClient("mongodb://localhost:27017/")

# Choose the database (or create one if it doesn't exist)
db = client['P1']

# Choose a collection (or create one if it doesn't exist)
collection = db['User']

# Example: Insert a document into the collection
document = {"name": "John Doe", "age": 30}
collection.insert_one(document)
result = collection.find_one({"name": "John Doe"})
print(result)
# Set up logging configurations