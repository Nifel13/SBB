import requests
import json
from Point import Point

API_URL = "https://journey-maps.api.sbb.ch/"
API_KEY = "bf9e3a88ab8101ba22ba8c752bbbcfd8"
auth = None

def getStation():
    response = requests.get(f"https://journey-maps.api.sbb.ch/path?api_key={API_KEY}", 
        headers = {
        'Authorization': f"Bearer {auth}",
        'accept': 'application/json',
        'Accept-Language': 'en',
        'Content-Type': 'application/json'
        })
    print(response.status_code)
    return response


def adress_to_coordinates(address):
    URL = f"https://geocode.maps.co/search?q={address}"
    response = requests.get(URL).json()

    return [float(response[0]["lat"]), float(response[0]["lon"])]


def getCarTrayectGeom(origin,destination):

    URL = 'https://api.openrouteservice.org/v2/directions/driving-car/geojson'    
    API_TOKEN = "5b3ce3597851110001cf6248dec7b9421134466185935f4d2665a1e0"
    headers = {
        "Accept": "application/geo+json",
        "Authorization": f'{API_TOKEN}',
        "Content-Type": "application/geo+json"
    }
    print(origin.lat, origin.lon)
    params = {
        "coordinates":[[origin.lon,origin.lat],[destination.lon,destination.lat]]
    }
    response = requests.post(f'{URL}',headers=headers,json=params).json()
    
    with open("traject.json", "w") as outfile:
        json.dump(response,outfile)    
    
    return response





