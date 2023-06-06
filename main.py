import json
import re
from fastapi import FastAPI

import latlon_api
from openai_api import generate_text
from common.constants import POSITIONSTACK_APIKEY, POSITIONSTACK_ENDPOINT
import facebook_api
import map
import data_layer.connection as mongo_connection
from apartments_api import router

app = FastAPI()
app.include_router(router)

def analyze_posts():
    mydb = mongo_connection.get_mongodb_connection()
    mycol = mydb["rental_ads"]

    posts = facebook_api.get_posts()
    cleaned_messages = []
    coords = []
    for p in posts:
        if p == "":
            continue

        cleaned_post = re.sub(r'[^א-ת\-."/:()a-z0-9 \n]+', '', p)
        print(cleaned_post)
        query = {"posting": cleaned_post}
        cur = mycol.find(query)
        results = list(cur)

        # if found in MongoDB no need to query OpenAI
        if len(results) == 0:
            cleaned_messages.append(cleaned_post)

            generated_text = generate_text(cleaned_post)
            print(generated_text)
            print(generated_text["choices"][0]["message"]["content"])
            print('--------------------\n')
            json_object = json.loads(generated_text["choices"][0]["message"]["content"])
            json_object["posting"] = cleaned_post
            address = json_object['address']
            lat, lon = latlon_api.get_coords(address)
            json_object["lat"], json_object["lon"] = lat, lon
            mycol.insert_one(json_object)
        else:
            print(f'found in DB: \n{results[0]}')
            address = results[0]['address']

    #map.produce_map(coords)

