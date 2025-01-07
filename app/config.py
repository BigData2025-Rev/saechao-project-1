import logging
import os
from pymongo import MongoClient
from dotenv import load_dotenv



# Load DB envirement variable
load_dotenv()


# Set base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME= os.getenv('DB_NAME')

client = MongoClient(f'mongodb://{DB_HOST}:{DB_PORT}/')


# Set up logging configurations