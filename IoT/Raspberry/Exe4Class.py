import requests
import json
import os
from meteo import *
from random import uniform
import time

# Replace 'your_api_key' with your actual OpenWeatherMap API key
ville = "casablanca"
api_key = '7702eb12505e07c7f2bc4041dc8cc00d'
api_url = f'http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}'

# Make the API request
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()

    # Convert temperature to Celsius
    #celsius_temperature = weather_data['main']['temp'] - 273.15

    # Add the Celsius temperature to the weather_data dictionary
    #weather_data['main']['temp_celsius'] = round(celsius_temperature, 2)

    # Create a Weather instance
    ##meteoINS = meteo(weather_data['main']['temp'], weather_data['main']['humidity'], weather_data['wind']['speed'], ville)

    # Accessing weather information
    ##print(f'Your city: {meteoINS.ville}%')
    ##print(f'Temperature: {meteoINS.get_temperature_celsius():.2f} °C')
    ##print(f'Humidity: {meteoINS.humidity}%')
    ##print(f'Wind Speed: {meteoINS.wind_speed} m/s')
    #curl -v -X POST http://thingsboard.cloud/api/v1/CPDhAlULqoenxQoLCHkD/telemetry --header Content-Type:application/json --data "{temperature:25}"
    #curl -v -X POST http://thingsboard.cloud/api/v1/q8ilo33p0nsz7z3v69x4/telemetry --header Content-Type:application/json --data "{temperature:25}"

    meteo_instance = meteo(weather_data)
    # Convert the instance data to a flat dictionary
    fweather_data = meteo_instance.to_flat_dict()
    while True:
        # List of keys to apply changes to
        keys_to_change = [
            'temperature_celsius', 'temperature_kelvin', 'temp_max_kelvin', 'humidity',
            'temp_min_kelvin', 'wind_speed', 'wind_deg'
        ]

        # Applying random changes to the specified keys
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
