from common.constants import POSITIONSTACK_APIKEY, POSITIONSTACK_ENDPOINT
import requests

def get_coords(address):
    # Send a GET request to the API
    params = {
        "access_key": POSITIONSTACK_APIKEY,
        "query": address
    }

    response = requests.get(POSITIONSTACK_ENDPOINT, params=params)
    # Parse the JSON response
    data = response.json()
    if "data" in data and len(data["data"]) > 0:
        location = data["data"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        return latitude, longitude
    else:
        print("Geocoding failed!")
        return None