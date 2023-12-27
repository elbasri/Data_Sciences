import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribe to the temperature and humidity topics
    client.subscribe("sensor/temperature")
    client.subscribe("sensor/humidity")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic == "sensor/temperature":
        print(f"Temperature: {str(msg.payload.decode())} °C")
    elif msg.topic == "sensor/humidity":
        print(f"Humidity: {str(msg.payload.decode())} %")

# Set up client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)  # Connect to the broker

# Blocking call that processes network traffic, dispatches callbacks, and handles reconnecting.
client.loop_forever()
