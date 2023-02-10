from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import requests
import json


def get_photo(city, state):
    # Create a dictionary for the headers to use in the request
    headers = {'Authorization': PEXELS_API_KEY}
    params = {
        "per_page": 1,
        "query": f'{city} {state}',
    }
    # Create the URL for the request with the city and state
    url = 'https://api.pexels.com/v1/search'
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    # Parse the JSON request
    content = json.loads(response.content)
    # Return a dictionary that contains a 'picture_url' key and
    #   one of the URLs for one of the pictures in the response
    try:
        return {'picture_url': content["photos"][0]["src"]["original"]}
    except KeyError:
        return {'picture_url': None}


def get_weather_data(city, state):
    headers = {"Authorization": OPEN_WEATHER_API_KEY}
    # Create the URL for the geocoding API with the city and state
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": f"{city},{state},USA",
        "appid": OPEN_WEATHER_API_KEY,
    }
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    # Parse the JSOn response
    content = json.loads(response.content)
    # Get the latitude and longitude from the response
    latitude = content[0]["lat"]
    longitude = content[0]["lon"]

    # Create the URL for the current weather API with the latitude
    #   and longitude
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": OPEN_WEATHER_API_KEY
    }
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    # Parse the JSON response
    content = json.loads(response.content)
    temperature = content["main"]["temp"]
    fahrenheit = 9 / 5 * (temperature - 273) + 32
    # Get the main tempeature and the weather's description and put
    #   them in a dictionary
    data = {
        "temp": round(fahrenheit, 2),
        "description": content["weather"][0]["description"],
    }
    # Return the dictionary
    return data
