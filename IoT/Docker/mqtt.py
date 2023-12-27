import random
import time
import paho.mqtt.client as mqtt
import json
import math

measurement = "sensorDataRaspPi"
mqtt_broker = "localhost"
mqtt_port = 1883
mqtt_topic = "/sensor/dht"
longitude = -0.1257
latitude = 51.5085
min_wind_speed = 0
max_wind_speed = 100
original_lat = 33.3820452
original_lon = -7.565208
radius = 10

def generate_random_location(lat, lon, radius):
    r = radius / 111.32
    u = random.random()
    v = random.random()
    w = r * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    new_x = x / math.cos(math.radians(lat))
    new_lat = lat + y
    new_lon = lon + new_x
    return new_lat, new_lon

def simulate_dht_sensor(client):
    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(40.0, 60.0), 2)
        wind_speed = round(random.uniform(min_wind_speed, max_wind_speed), 2)
        atmospheric_pressure = round(random.uniform(980, 1050), 2)
        light_intensity = round(random.uniform(0, 1000), 2)
        latitude, longitude = generate_random_location(original_lat, original_lon, radius)
        payload = json.dumps({
            "measurement": measurement,
            "temperature": temperature,
            "humidity": humidity,
            "longitude": longitude,
            "latitude": latitude,
            "wind_speed": wind_speed,
            "atmospheric_pressure": atmospheric_pressure,
            "light_intensity": light_intensity
        })
        result = client.publish(mqtt_topic, payload)
        print(f"Sent data: {payload}")
        print(f"Result: {result}")
        time.sleep(5)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to MQTT broker.")
    else:
        print(f"Connection failed with code {rc}.")

client = mqtt.Client()
client.on_connect = on_connect

try:
    client.connect(mqtt_broker, mqtt_port, 60)
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

client.loop_start()
simulate_dht_sensor(client)
