from fastapi import HTTPException
from bson import ObjectId

from data_layer.connection import get_mongodb_connection

db = get_mongodb_connection()
rentals_collection = db["post_data"]

def get_rental_ads():
    rentals = list(rentals_collection.find())
    for rental in rentals:
        rental["_id"] = str(rental["_id"])

    return rentals

def get_rental_ad_filter(filters):
    """Gets a user by ID."""
    query = dict()
    for key, value in filters.items():
        if value is not None:
            query[key] = value
            if key == 'price' and value is not None:
                # query pymongo for a range
                low, high = value.split('-')
                query["price"] = {"$gte": int(low), "$lte": int(high)}
            if key == '_id' and value is not None:
                query['_id'] = ObjectId(value)

    print(query)
    rentals = list(rentals_collection.find(query))

    for rental in rentals:
        rental["_id"] = str(rental["_id"])

    return rentals

def create_posting():
    pass