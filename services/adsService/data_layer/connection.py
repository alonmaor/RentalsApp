import pymongo
from common.constants import MONGO_URI, MONGO_DB_NAME

def get_mongodb_connection():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    return db