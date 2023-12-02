import json
import requests

ID = "0"
format="png"
API_URL = f'https://journey-maps-tiles.geocdn.sbb.ch/styles/base_bright_v2/style/{ID}/sprite.{format}'
API_KEY = "8ff1e3c393578b6463f8a24b6baf0fd6"


aa = requests.get(f'{API_URL}?api_key={API_KEY}')
print(aa)

print(aa.json())
