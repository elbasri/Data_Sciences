class meteo:
    def __init__(self, temperature_kelvin, humidity, wind_speed, ville):
        self.temperature_kelvin = temperature_kelvin
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.ville = ville

    def get_temperature_celsius(self):
        return self.temperature_kelvin - 273.15
