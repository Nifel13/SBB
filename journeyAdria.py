import requests
import json
from math import sqrt
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

def use_token_serv(origin, destination, date, time):
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

def read_params_from_json():
    with open('mobilitat.json', 'r') as f:
        params = json.load(f)
    return params

def coords_parkrail(place, params):
    for i in range(len(params)):
        if str(params[i]['bpuic']) == place['places'][0]['id']:
            return params[i]['geopos']['lon'], params[i]['geopos']['lat']
        
def time_per_vehicle(vehicle, coord_start, coord_end):
    pass

def place(lon, lat):
    place = use_token_places(lon, lat)
    id_place = place['places'][0]['id']
    coords_place = place['places'][0]['centroid']['coordinates']
    return place, id_place, coords_place


class Train:
    def __init__(self, start, end):
        date = datetime.now()
        self.start = start
        self.end = end
        formatted_date = date.strftime("%Y-%m-%d")
        self.day = str(formatted_date)
        self.hour = str(date.strftime("%H:%M"))
        self.best_destinations = []
        for i in range(len(use_token_serv(self.start, self.end, "2023-04-18", "13:07")['trips'])):
            self.best_destinations.append(use_token_serv(self.start, self.end, "2023-04-18", "13:07")['trips'][i])

    def heurizztic(self):
        best_train = [None,999999999]
        for viatge in self.best_destinations:
            puntuacio = 0
            puntuacio += hour_to_min(viatge)
            puntuacio += len(viatge['legs'])*10
            if puntuacio < best_train[1]:
                best_train[0] = viatge
                best_train[1] = puntuacio
        print('heuristic points: ',best_train[1], "time:", hour_to_min(best_train[0]), "Transfers: ", len(best_train[0]['legs']))
        return best_train[0]
    
class Walk:
    def __init__(self, coord_start, coord_end):
        self.coord_start = coord_start
        self.coord_end = coord_end
    def get_time(self):
        return time_per_vehicle('walk', self.coord_start, self.coord_end)

class Car:
    def __init__(self, coord_start, coord_end):
        self.coord_start = coord_start
        self.coord_end = coord_end

    def get_time(self):
        return time_per_vehicle('car', self.coord_start, self.coord_end)

    
class Journey:
    def __init__(self, car, walk1, train, walk2):
        self.car = car
        self.walk1 = walk1
        self.train = train
        self.walk2 = walk2

    def total_time(self):
        return 10 + 5 + hour_to_min(self.train.heurizztic()) + 6
    

if __name__ == '__main__':
    A = [8.544152, 47.411525]
    B = [6.630315, 46.520677]
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

    car = Car(A, coords_pr)
    walk1 = Walk(coords_pr, coords_place_a)
    train = Train(str(id_place_a), str(id_place_b))
    walk2 = Walk(coords_place_b, B)

    results = Journey(car, walk1, train, walk2)
    print(results.total_time())

'''def coordinates_to_id(lat,long):
    temp = use_token_serv(self.start, self.end, self.day, self.hour)

bubuselo = Journey("8503000","8507000")
bubuselo.heurizztic()
    
print(coordinates_to_station(8.540193, 47.378177))'''
