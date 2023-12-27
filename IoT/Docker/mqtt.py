# Import des bibliothèques nécessaires
import random
import time
import paho.mqtt.client as mqtt

# Nom de la mesure
Measurement ="sensorData"
# Configuration MQTT
mqtt_broker = "localhost"
mqtt_port = 1883
mqtt_topic = "/sensor/dht"

# Fonction de simulation du capteur DHT
def simulate_dht_sensor():
    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(40.0, 60.0), 2)

        # Formatage des données en JSON
        payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'

        # Envoi des données via MQTT
        clnt = client.publish(mqtt_topic, payload)
        print(f"Sent data: {payload}")
        print(f"CLNT: {clnt}")

        time.sleep(5)  # Intervalle de simulation en secondes

# Configuration du client MQTT
client = mqtt.Client()
clntC = client.connect(mqtt_broker, mqtt_port, 60)
print(f"CLIENT: {clntC}")

# Lancement de la simulation du capteur DHT
simulate_dht_sensor()