import paho.mqtt.publish as publish
import random
import time

# MQTT server details
broker = "localhost"
port = 1883

# Simulate sensor data
def simulate_sensor_data():
    temperature = round(random.uniform(20, 30), 2)  # Simulate temperature (20°C to 30°C)
    humidity = round(random.uniform(30, 60), 2)     # Simulate humidity (30% to 60%)
    return temperature, humidity

while True:
    # Generate sensor data
    temp, hum = simulate_sensor_data()

    # Create the payload
    payload_temp = f"{temp}"
    payload_hum = f"{hum}"

    # Publish the message to topics
    publish.single("sensor/temperature", payload_temp, hostname=broker, port=port)
    publish.single("sensor/humidity", payload_hum, hostname=broker, port=port)
    
    print(f"Published - Temperature: {payload_temp} °C, Humidity: {payload_hum} %")

    # Wait before sending the next set of data
    time.sleep(5)  # 5 seconds interval
