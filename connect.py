from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os


mongo_url = os.getenv('MONGO_URI')
mongo_client = MongoClient(mongo_url)
db=mongo_client['todo_db']
task_collection = db['task']


