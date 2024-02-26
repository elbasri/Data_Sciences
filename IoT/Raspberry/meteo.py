class meteo:
    def __init__(self, weather_data):
        self.data = weather_data

    def get_temperature_celsius(self):
        return self.data['main']['temp'] - 273.15

    def to_flat_dict(self):

        flat_data = {
            'city': self.data['name'],
            'temperature_celsius': self.get_temperature_celsius(),
            'longitude': self.data['coord']['lon'],
            'latitude': self.data['coord']['lat'],
            'weather_id': self.data['weather'][0]['id'],
            'weather_main': self.data['weather'][0]['main'],
            'weather_description': self.data['weather'][0]['description'],
            'weather_icon': self.data['weather'][0]['icon'],
            'base': self.data['base'],
            'temperature_kelvin': self.data['main']['temp'],
            'feels_like_kelvin': self.data['main']['feels_like'],
            'temp_min_kelvin': self.data['main']['temp_min'],
            'temp_max_kelvin': self.data['main']['temp_max'],
            'pressure': self.data['main']['pressure'],
            'humidity': self.data['main']['humidity'],
            'visibility': self.data.get('visibility', None),
            'wind_speed': self.data['wind']['speed'],
            'wind_deg': self.data['wind']['deg'],
            'clouds_all': self.data['clouds']['all'],
            'dt': self.data['dt'],
            'sys_type': self.data['sys']['type'],
            'sys_id': self.data['sys']['id'],
            'country': self.data['sys']['country'],
            'sunrise': self.data['sys']['sunrise'],
            'sunset': self.data['sys']['sunset'],
            'timezone': self.data['timezone'],
            'city_id': self.data['id'],
            'cod': self.data['cod']
        }
        return flat_data
