import requests
import json

API_URL = "https://journey-service-int.api.sbb.ch"
API_KEY = "bf9e3a88ab8101ba22ba8c752bbbcfd8"
auth = None

response = requests.get(f"https://journey-service-int.api.sbb.ch?api_key={API_KEY}", 
    headers = {
    'Authorization': f"Bearer {auth}",
    'accept': 'application/json',
    'Accept-Language': 'en',
    'Content-Type': 'application/json'
    })
print(response.status_code)