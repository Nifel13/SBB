import requests
import json

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
def use_token_places(longitude, latitude):
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

def read_params_from_json():
    with open('mobilitat.json', 'r') as f:
        params = json.load(f)
    return params

def coords_parkrail(place, params):
    for i in range(len(params)):
        if str(params[i]['bpuic']) == place['places'][0]['id']:
            return params[i]['geopos']['lon'], params[i]['geopos']['lat']

'''if __name__ == '__main__':
    longitude = 8.5441
    latitude = 47.4115
    place = use_token_places(longitude, latitude)
    coords_place = place['places'][0]['centroid']['coordinates']
    params = read_params_from_json()
    coords_parktrail = coords_parkrail(place, params)
    print(coords_parktrail)'''

if __name__ == '__main__':
    A = [8.544152, 47.411525]
    B = A
    longitude_a, latitude_a = A
    longitude_b, latitude_b = B

    place_a = use_token_places(longitude_a, latitude_a)
    id_place_a = place_a['places'][0]['id']
    coords_place_a = place_a['places'][0]['centroid']['coordinates']
    params = read_params_from_json()
    coords_pr = coords_parkrail(place_a, params)

    place_b = use_token_places(longitude_b, latitude_b)
    id_place_b = place_b['places'][0]['id']
    coords_place_b = place_b['places'][0]['centroid']['coordinates']


