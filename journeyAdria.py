import requests
import pandas as pd
from tabulate import tabulate

API_URL = "https://journey-service-int.api.sbb.ch"
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

    response = requests.post("https://journey-service-int.api.sbb.ch/v3/trips/by-origin-destination", headers=headers, json={
        "origin": origin,
        "destination": destination,
        "date": date,
        "time": time,
    }).json()

    return response


best_destinations = []

for i in range(len(use_token("8503000", "8507000", "2023-04-18", "13:07")['trips'])):
    best_destinations.append(use_token("8503000", "8507000", "2023-04-18", "13:07")['trips'][i]['duration'])

print(best_destinations)


