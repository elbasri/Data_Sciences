import paho.mqtt.client as mqtt

# MQTT broker details
broker = "172.20.10.7"
port = 1883
topic = "pingtest"

print("Begin")
# Callback when connecting to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic)  # Subscribe to the topic
    else:
        print("Failed to connect, return code %d\n", rc)

# Callback when receiving a message from the MQTT broker
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    if msg == "Ping":
        print("Ping received!")
    else:
        print(f"Received message '{msg}' on topic '{message.topic}'")

# Set up the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(broker, port, 60)  # Connect to the broker

client.loop_start()  # Start the loop
print(client.on_connect)
# Send a single message (Ping)
client.publish(topic, "Ping")

# Wait to receive the message back (or for a timeout)
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
