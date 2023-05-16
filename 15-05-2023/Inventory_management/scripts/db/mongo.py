from scripts.constant.db_constant import db_constant_object
from pymongo import MongoClient


client = MongoClient(db_constant_object.uri)
db = client[db_constant_object.database_name]
collection = db[db_constant_object.collection_name]
