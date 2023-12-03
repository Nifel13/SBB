import requests
import json

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


