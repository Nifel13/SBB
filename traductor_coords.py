import requests
import json
from geopy.geocoders import Nominatim

API_URL = "https://journey-service-int.api.sbb.ch/"
CLIENT_SECRET = "MU48Q~IuD6Iawz3QfvkmMiKHtfXBf-ffKoKTJdt5"
CLIENT_ID = "f132a280-1571-4137-86d7-201641098ce8"
SCOPE = "c11fa6b1-edab-4554-a43d-8ab71b016325/.default"


def get_token():
    params = {
        'grant_type': 'client_credentials',
        'scope': SCOPE,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    return requests.get('https://login.microsoftonline.com/2cda5d11-f0ac-46b3-967d-af1b2e1bd01a/oauth2/v2.0/token',
                         data=params).json()

# Longitude and latitude with 4 decimals (both are strings)
def use_token(longitude, latitude):
    auth = get_token()['access_token']
    headers = {
        'Authorization': f"Bearer {auth}",
        'accept': 'application/json',
        'Accept-Language': 'en',
        'Content-Type': 'application/json'
    }

    response = requests.get("https://journey-service-int.api.sbb.ch/v3/places/by-coordinates", headers=headers, params={
        "longitude": longitude,
        "latitude": latitude,
    }).json()

    return response

def trans_coords(longitude, latitude):
    return use_token(longitude, latitude)["places"][0]["id"]


def get_coordinates(location):
    # Create a geocoder using Nominatim
    geolocator = Nominatim(user_agent="my_geocoder")

    # Use the geocoder to get the location coordinates
    location_data = geolocator.geocode(location)

    if location_data:
        # Extract latitude and longitude
        latitude, longitude = location_data.latitude, location_data.longitude
        return latitude, longitude
    else:
        print("Location not found.")
        return None




