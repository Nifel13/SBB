import requests
import json

API_URL_discord = "https://journey-maps-tiles.api.sbb.ch/"
API_URL = "https://journey-maps-tiles.geocdn.sbb.ch/styles/base_bright_v2/style.json"
API_KEY = "8ff1e3c393578b6463f8a24b6baf0fd6"
ID = None
format = "png"

response = requests.get(f"{API_URL}?api_key={API_KEY}")
response["platform_nr"]

 
# Writing to sample.json
with open("./MapUserInterface/map_json.json", "w") as outfile:
    json.dump(response.json(), outfile)