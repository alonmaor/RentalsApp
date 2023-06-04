from pydantic import BaseModel
from fastapi import APIRouter

from data_layer.connection import get_mongodb_connection

# MongoDB connection
db = get_mongodb_connection()
rentals_collection = db["post_data"]
router = APIRouter()

# Rental model
class Rental(BaseModel):
    address: str
    price: int
    rooms: int
    elevator: bool
    petsAllowed: bool

# API endpoint to get rentals
@router.get("/get_rentals")
def get_rentals():
    rentals = list(rentals_collection.find())
    for rental in rentals:
        rental["_id"] = str(rental["_id"])
    return rentals


# Include the router in the main FastAPI app
from main import app
app.include_router(router)