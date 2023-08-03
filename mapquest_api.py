import googlemaps
import requests
from common.constants import MAPQUEST_APIKEY_NAME, MAPQUEST_ENDPOINT_NAME

GOOGLE_APIKEY = 'AIzaSyByFNmQ6o10zjjuabg6N-54K7tSytzfv7k'


def google_geocode(address):
    gmaps = googlemaps.Client(key=GOOGLE_APIKEY)

    # Geocode the address
    if address is None or address == '':
        return None
    geocode_result = gmaps.geocode(address=address+', Tel Aviv', region='IL')

    print(f'geocode_result: {geocode_result}')
    if len(geocode_result) == 0:
        return None

    # Get the latitude and longitude from the geocode result
    latitude = geocode_result[0]["geometry"]["location"]["lat"]
    longitude = geocode_result[0]["geometry"]["location"]["lng"]

    location = {'latitude': latitude, 'longitude': longitude}

    return location



def geocode(address, neighborhood, config):
    apikey = config[MAPQUEST_APIKEY_NAME]
    url = config[MAPQUEST_ENDPOINT_NAME]
    location = address + ', ' + neighborhood + ', Tel Aviv'
    params = {
        "location": location,
        "key": apikey
    }
    response = requests.get(url, params=params)
    status_code = response.json()["info"]["statuscode"]
    print(f'status_code: {response.json()}')

    if status_code in [0,200]:
        print(response.json())
        location = dict()
        location["latitude"] = response.json()["results"][0]["locations"][0]["latLng"]["lat"]
        location["longitude"] = response.json()["results"][0]["locations"][0]["latLng"]["lng"]
        return location
    else:
        return None