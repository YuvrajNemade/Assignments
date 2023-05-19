from scripts.constant.app_constant import db_constant_object
from pymongo import MongoClient
from scripts.logging.logs import logger


try:
    client = MongoClient(db_constant_object.uri)
    db = client[db_constant_object.database_name]
    collection = db[db_constant_object.collection_name]
except Exception as e:
    logger.error({"Error:", "while connecting to MongoDB"})