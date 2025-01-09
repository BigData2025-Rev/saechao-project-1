import logging
import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME= os.getenv('DB_NAME')

logging.basicConfig(
    filename='logs/app.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)


def get_db():
    client = MongoClient(f'mongodb://{DB_HOST}:{DB_PORT}/')
    return client[DB_NAME]

def log_event(event):
    logging.info(event)

