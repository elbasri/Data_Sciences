import paho.mqtt.publish as publish
import random
import time

broker = "localhost"
port = 1883

# Simulation de DHT
def simulate_sensor_data():
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(30, 60), 2)
    return temperature, humidity

while True:
    temp, hum = simulate_sensor_data()

    payload_temp = f"{temp}"
    payload_hum = f"{hum}"

    publish.single("sensor/temperature", payload_temp, hostname=broker, port=port)
    publish.single("sensor/humidity", payload_hum, hostname=broker, port=port)
    
    print(f"Published - Temperature: {payload_temp} °C, Humidity: {payload_hum} %")

    time.sleep(5)
