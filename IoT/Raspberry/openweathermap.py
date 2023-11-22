import requests
import json
import os

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = '7702eb12505e07c7f2bc4041dc8cc00d'
city_name = 'casablanca'
api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

# Make the API request
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()

    # Convert temperature to Celsius
    celsius_temperature = weather_data['main']['temp'] - 273.15

    # Add the Celsius temperature to the weather_data dictionary
    weather_data['main']['temp_celsius'] = round(celsius_temperature, 2)

    # Create a 'data' folder if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Save the modified weather data to a JSON file in the 'data' folder
    with open('data/weather_data.json', 'w') as file:
        json.dump(weather_data, file, indent=2)

    print(f'Temperature in Celsius: {celsius_temperature:.2f} °C')
    print('Weather data has been successfully saved to data/weather_data.json')
else:
    print(f'Error {response.status_code}: Unable to fetch weather data')
    print(response.text)
