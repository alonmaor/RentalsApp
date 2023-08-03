from fastapi import HTTPException
from bson import ObjectId
import logging

from data_layer.connection import get_mongodb_connection

db = get_mongodb_connection()
rentals_collection = db["rental_ads"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('rental_ads.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def get_rental_ads():
    rentals = list(rentals_collection.find())
    for rental in rentals:
        rental["_id"] = str(rental["_id"])

    return rentals

def get_rental_ad_filter(filters):
    """Gets a user by ID."""
    query = dict()
    for key, value in filters.items():
        logger.info(f'filter key: {key}, value: {value}, value type: {type(value)}')
        if value is not None:
            query[key] = value
            if key == 'price' and value is not None:
                # query pymongo for a range
                low, high = value.split('-')
                query['price'] = {"$gte": int(low), "$lte": int(high)}
            if key == '_id' and value is not None:
                query['_id'] = ObjectId(value)
            if key == 'createdDate':
                query['createdDate'] = {'$exists': True, "$eq": value}
                # if '-' in value:
                #     low, high = value.split('-')
                #     query["createdDate"] = {"$gte": low, "$lte": high}
                # else:
                #     query["createdDate"] = value

    print(query)
    rentals = list(rentals_collection.find(query))

    for rental in rentals:
        rental["_id"] = str(rental["_id"])

    return rentals

def create_posting():
    pass