from fastapi import HTTPException
from bson import ObjectId
from data_layer.connection import get_mongodb_connection

db = get_mongodb_connection()
rentals_collection = db["rental_ads"]

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
            elif key == '_id' and value is not None:
                query['_id'] = ObjectId(value)
            elif key == 'createdDate':
                if '-' in value:
                    low, high = value.split('-')
                    query["createdDate"] = {"$gte": low, "$lte": high}
                else:
                    query["createdDate"] = ISODate(value)

    print(query)
    rentals = list(rentals_collection.find(query))

    for rental in rentals:
        rental["_id"] = str(rental["_id"])

    return rentals

def create_posting():
    pass