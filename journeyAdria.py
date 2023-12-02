import requests
import pandas as pd
from tabulate import tabulate
from datetime import datetime

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

def hour_to_min(travel):
    duration = travel['duration']
    parts = duration[2:].split('H')
    if len(parts) == 1:
        hours = 0
        minutes = int(parts[0][:-1])
    else:
        hours = int(parts[0])
        minutes = int(parts[1][:-1])
    return hours * 60 + minutes


class Journey:

    def __init__(self,start,end):
        date = datetime.now()
        self.start = start
        self.end = end
        formatted_date = date.strftime("%Y-%m-%d")
        self.day = formatted_date
        self.hour = str(datetime.now().hour) + ":" + str(datetime.now().minute)
        self.best_destinations = []
        for i in range(len(use_token(self.start, self.end, "2023-04-18", "13:07")['trips'])):
            self.best_destinations.append(use_token(self.start, self.end, "2023-04-18", "13:07")['trips'][i])
            

    

    def heurizztic(self):
        best_train = [None,999999999]
        for viatge in self.best_destinations:
            puntuacio = 0
            puntuacio += hour_to_min(viatge)
            puntuacio += len(viatge['legs'])*10
            if puntuacio < best_train[1]:
                best_train[0] = viatge
                best_train[1] = puntuacio
        print('heuristic points: ',best_train[1], "time:" ,hour_to_min(best_train[0]), "Transfers: ", len(best_train[0]['legs']))
        return best_train[0]
        
    


bubuselo = Journey("8503000","8507000")
bubuselo.heurizztic()

