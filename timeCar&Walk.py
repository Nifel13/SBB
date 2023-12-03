import requests

def get_travel_time(coordinates_origin, coordinates_destination, api_key, mode):
    # Mode can be 'driving-car' for car or 'foot-walking' for walking
    url = f"https://api.openrouteservice.org/v2/directions/{mode}?api_key={api_key}&start={coordinates_origin}&end={coordinates_destination}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        travel_time_seconds = data['features'][0]['properties']['segments'][0]['duration']
        travel_time_minutes = travel_time_seconds / 60

        return travel_time_minutes

    except requests.exceptions.RequestException as e:
        print(f"Error in API request: {e}")
        return None

# Example of usage
if __name__ == "__main__":
    api_key = '5b3ce3597851110001cf6248dec7b9421134466185935f4d2665a1e0'
    coordinates_origin = '-76.976660,38.847240'  # For example, Washington, DC
    coordinates_destination = '-77.036870,38.907190'  # For example, Washington, DC

    # Get travel time by car
    travel_time_car = get_travel_time(coordinates_origin, coordinates_destination, api_key, 'driving-car')

    # Get travel time walking
    travel_time_walking = get_travel_time(coordinates_origin, coordinates_destination, api_key, 'foot-walking')

    if travel_time_car is not None:
        print(f"The travel time by car is {travel_time_car:.2f} minutes.")

    if travel_time_walking is not None:
        print(f"The travel time walking is {travel_time_walking:.2f} minutes.")
