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


#test = use_token(8.5441, 47.4115)
#print(test["places"][0]["id"])

def read_params_from_json():
    with open('park_rail.json', 'r') as f:
        params = json.load(f)
    return params

params = read_params_from_json()

for i in range(params['total_count']):
    pass