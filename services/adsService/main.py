from typing import Union

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from data_layer import operations

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API endpoint to get rentals
# @app.get("/rental_ads/all")
# def get_rentals(query: RentalFilter):
#     rental_ads = operations.get_rental_ads()
#
#     return rental_ads

def check_params():
    pass
@app.get("/rental_ads")
def get_rental(
        _id: str = Query(None),
        rooms: Union[int, None] = Query(None),
        price: Union[str, None] = Query(None),
        elevator: Union[bool, None] = Query(None),
        petsAllowed: Union[bool, None] = Query(None),
        mediation: Union[bool, None] = Query(None)):
    filters = {
        '_id': _id,
        'rooms': rooms,
        'price': price,
        'elevator': elevator,
        'petsAllowed': petsAllowed,
        'mediation': mediation
    }

    rental_ad = operations.get_rental_ad_filter(filters)

    return rental_ad
