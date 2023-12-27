# Import necessary libraries
import random
import time
import paho.mqtt.client as mqtt
import json

# Measurement name
measurement = "sensorData"

# MQTT Configuration
mqtt_broker = "localhost"
mqtt_port = 1883
mqtt_topic = "/sensor/dht"

# Function to simulate DHT sensor readings
def simulate_dht_sensor(client):
    while True:
        # Generate random temperature and humidity values
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(40.0, 60.0), 2)

        # Format the data as a JSON string
        payload = json.dumps({
            "measurement": measurement,
            "temperature": temperature,
            "humidity": humidity
        })

        # Send the data via MQTT
        result = client.publish(mqtt_topic, payload)

        # Print the sent data and result of the publish operation
        print(f"Sent data: {payload}")
        print(f"Result: {result}")

        # Wait for a specified interval before sending the next set of data
        time.sleep(5)

# Callback for successful connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to MQTT broker.")
    else:
        print(f"Connection failed with code {rc}.")

# Setup MQTT client
client = mqtt.Client()

# Assign the on_connect callback function
client.on_connect = on_connect

# Connect to the MQTT broker
try:
    client.connect(mqtt_broker, mqtt_port, 60)
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

# Start the MQTT client loop in a separate thread
client.loop_start()

# Start simulating the DHT sensor
simulate_dht_sensor(client)
