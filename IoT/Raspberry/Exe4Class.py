import requests
import json
import os
from meteo import *
from random import uniform
import time

ville = "casablanca"
api_key = '7702eb12505e07c7f2bc4041dc8cc00d'
api_url = f'http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}'

# Make the API request
response = requests.get(api_url)

if response.status_code == 200:
    weather_data = response.json()

    meteo_instance = meteo(weather_data)
    fweather_data = meteo_instance.to_flat_dict()
    while True:
        keys_to_change = [
            'temperature_celsius', 'temperature_kelvin', 'temp_max_kelvin', 'humidity',
            'temp_min_kelvin', 'wind_speed', 'wind_deg'
        ]

        for key in keys_to_change:
            if key in fweather_data:
                change_factor = uniform(-1, 2)
                if(fweather_data[key] < 1) :
                    change_factor = uniform(1, 1)
                fweather_data[key] += change_factor
        print("Changed")
        print(fweather_data)
        url = "http://thingsboard.cloud/api/v1/q8ilo33p0nsz7z3v69x4/telemetry"
        headers = {"Content-Type": "application/json"}
        data = json.dumps(fweather_data)

        response = requests.post(url, headers=headers, data=data)
        print(response)
        time.sleep(5)
else:
    print(f'Error {response.status_code}: Unable to fetch weather data')
    print(response.text)
