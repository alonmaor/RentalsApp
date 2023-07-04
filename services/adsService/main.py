from typing import Union

from bson import ObjectId
from fastapi import FastAPI, Query
from pydantic import BaseModel, typing

from data_layer import operations

app = FastAPI()

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


if __name__ == '__main__':
    print('test')
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)