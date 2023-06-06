from fastapi import FastAPI

from services.adsService.data_layer.connection import get_mongodb_connection

# MongoDB connection
db = get_mongodb_connection()
rentals_collection = db["post_data"]
app = FastAPI()

# API endpoint to get rentals
@app.get("/rental_ads")
def get_rentals():
    rentals = list(rentals_collection.find())
    for rental in rentals:
        rental["_id"] = str(rental["_id"])
    return rentals

# if __name__ == '__main__':
#     #analyze_posts()
#
#     import uvicorn
#
#     uvicorn.run("main:app", host="localhost", port=8000, reload=True)
# # Include the router in the main FastAPI app