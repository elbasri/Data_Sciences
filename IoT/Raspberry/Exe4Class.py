import requests
import json
import os
from meteo import *

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
    meteoINS = meteo(weather_data['main']['temp'], weather_data['main']['humidity'], weather_data['wind']['speed'], ville)

    # Accessing weather information
    print(f'Your city: {meteoINS.ville}%')
    print(f'Temperature: {meteoINS.get_temperature_celsius():.2f} °C')
    print(f'Humidity: {meteoINS.humidity}%')
    print(f'Wind Speed: {meteoINS.wind_speed} m/s')
else:
    print(f'Error {response.status_code}: Unable to fetch weather data')
    print(response.text)
