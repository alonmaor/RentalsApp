import json
import os
import re
import logging

import latlon_api
from openai_api import generate_text
from common.constants import POSITIONSTACK_APIKEY_NAME, POSITIONSTACK_ENDPOINT_NAME, OPENAI_APIKEY_NAME, \
    FB_ACCESS_TOKEN_NAME, FB_GROUP_ID_NAME
import facebook_api
import data_layer.connection as mongo_connection


def analyze_posts(config):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler('example.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    mydb = mongo_connection.get_mongodb_connection()
    mycol = mydb["rental_ads"]

    # posts = facebook_api.get_fb_posts(config, logger)
    cleaned_messages = []
    for post in facebook_api.scrape_fb_posts(config, logger):
        p = post['text']
        if p == "":
            continue

        cleaned_post = re.sub(r'[^א-ת\-."/:()a-zA-Z0-9 \n]+', '', p)
        logger.info(cleaned_post)
        query = {"posting": cleaned_post}
        cur = mycol.find(query)
        results = list(cur)

        print(f'------------------cleaned_post-------------------\n{cleaned_post}')
        # if found in MongoDB no need to query OpenAI
        if len(results) == 0:
            cleaned_messages.append(cleaned_post)

            generated_text = generate_text(cleaned_post, config)

            logger.info(f'-------------------generated_text-------------------\n{generated_text}')
            # logger.info(generated_text["choices"][0]["message"]["content"])
            logger.info('----------------------------------------------------------\n')
            json_object = json.loads(generated_text["choices"][0]["message"]["content"])
            json_object["posting"] = cleaned_post
            address = json_object['address']
            location = latlon_api.get_coords(address, config, logger)
            if location is not None:
                lat = location["latitude"]
                lon = location["longitude"]
                json_object["lat"], json_object["lon"] = lat, lon
            logger.info(f'-------------------json object-------------------\n{json_object}')
            logger.info('----------------------------------------------------------\n')
            print()
            print(f'-------------------json object-------------------\n{json_object}')
            mycol.insert_one(json_object)
        else:
            logger.info(f'found in DB: \n{results[0]}')
            print(f'found in DB: \n{results[0]}')
            address = results[0]['address']

        print('----------------------------------------\n\n')

    #map.produce_map(coords)


def load_config():
    # load values from environment variables
    config = dict()

    config[POSITIONSTACK_APIKEY_NAME] = os.getenv(POSITIONSTACK_APIKEY_NAME)
    config[POSITIONSTACK_ENDPOINT_NAME] = os.getenv(POSITIONSTACK_ENDPOINT_NAME)
    config[OPENAI_APIKEY_NAME] = os.getenv(OPENAI_APIKEY_NAME)
    config[FB_ACCESS_TOKEN_NAME] = os.getenv(FB_ACCESS_TOKEN_NAME)
    config[FB_GROUP_ID_NAME] = os.getenv(FB_GROUP_ID_NAME)

    return config


if __name__ == '__main__':
    config = load_config()

    analyze_posts(config)