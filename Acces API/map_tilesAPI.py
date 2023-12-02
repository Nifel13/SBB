import requests
import json

API_URL = "https://journey-service-int.api.sbb.ch/"
API_KEY = "bf9e3a88ab8101ba22ba8c752bbbcfd8"
ID = None

response = requests.get(f"{API_URL}?api_key={API_KEY}")


print(response.status_code)