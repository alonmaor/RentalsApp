from common.constants import POSITIONSTACK_APIKEY_NAME, POSITIONSTACK_ENDPOINT_NAME
import requests

def get_coords(address, config, logger):
    # Send a GET request to the API
    apikey = config[POSITIONSTACK_APIKEY_NAME]
    endpoint = config[POSITIONSTACK_ENDPOINT_NAME]
    params = {
        "access_key": apikey,
        "query": address
    }

    response = requests.get(endpoint, params=params)
    # Parse the JSON response
    data = response.json()
    if "data" in data and len(data["data"]) > 0:
        location = data["data"][0]

        if type(location) is not dict:
            logger.info(f'Geocoding failed. Address is invalid. \n {location}')
            return None

        return location
    else:
        logger.info("Geocoding failed!")
        return None