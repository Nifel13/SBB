import requests
import pandas as pd


API_URL = "https://journey-service-int.api.sbb.ch"
URL_ROAD = "/v3/INCUBATOR/trips/by-road"
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
    return requests.post('https://login.microsoftonline.com/2cda5d11-f0ac-46b3-967d-af1b2e1bd01a/oauth2/v2.0/token',
                         data=params).json()

def use_token(origin, destination, date, time):
    auth = get_token()['access_token']
    headers = {
        'Authorization': f"Bearer {auth}",
        'accept': 'application/json',
        'Accept-Language': 'en',
        'Content-Type': 'application/json'
    }

    response = requests.post(f'{API_URL}{URL_ROAD}', headers=headers, json={
        "origin": origin,
        "destination": destination,
        "date": date,
        "time": time,
    }).json()
    return response


def getByRoad(origin, destination):
    '''
    origin and destination: id (seguramente estacion) o coords
    '''
    auth = get_token()['access_token']
    headers = {
        'Authorization': f"Bearer {auth}",
        'accept': 'application/json',
        'Accept-Language': 'en',
        'origin':f'{origin}',
        'destination':f'{destination}'
    }
    response = requests.get(f'{API_URL}{URL_ROAD}', headers=headers)
    return response


print(getByRoad("8503000","8507000"))
#print(use_token("[46.516606, 6.629825]","[46.475691, 6.399441]","2023-12-02","13:05"))
