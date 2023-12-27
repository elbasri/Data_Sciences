#include <WiFi.h>
#include <PubSubClient.h>
#include <DHTesp.h>

const int DHT_PIN = 15;
DHTesp dht;
const char* ssid = "Wokwi-GUEST";
const char* password = "";
const char* mqtt_server = "test.mosquitto.org";
const int mqtt_port = 1883;
WiFiClient espClient;
PubSubClient client(espClient);
const char* temp_topic = "/Mundiapolis/temp";
const char* hum_topic = "/Mundiapolis/hum";
const char* welcome_topic = "/Mundiapolis/Publish";
const char* subscribe_topic = "/Mundiapolis/Subscribe";
unsigned long lastMsg = 0;
const long publish_interval = 2000;

void connectToWiFi() {
  Serial.println("\nConnexion au WiFi...");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connecté");
  Serial.print("Adresse IP: ");
  Serial.println(WiFi.localIP());
}

void mqttCallback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message MQTT reçu [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void reconnectToMQTT() {
  while (!client.connected()) {
    Serial.print("Tentative de connexion MQTT...");
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);
    if (client.connect(clientId.c_str())) {
      Serial.println("Connecté");
      client.publish(welcome_topic, "Bonjour de l'ESP32");
      client.subscribe(subscribe_topic);
    } else {
      Serial.print("Échec, rc=");
      Serial.print(client.state());
      Serial.println(" Nouvel essai dans 5 secondes");
      delay(5000);
    }
  }
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  connectToWiFi();
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(mqttCallback);
  dht.setup(DHT_PIN, DHTesp::DHT22);
}

void loop() {
  if (!client.connected()) {
    reconnectToMQTT();
  }
  client.loop();
  unsigned long now = millis();
  if (now - lastMsg > publish_interval) {
    lastMsg = now;
    TempAndHumidity data = dht.getTempAndHumidity();
    if (dht.getStatus() == 0) {
      String tempStr = String(data.temperature, 2);
      String humStr = String(data.humidity, 1);
      if (!tempStr.equals("NaN") && !humStr.equals("NaN")) {
        client.publish(temp_topic, tempStr.c_str());
        client.publish(hum_topic, humStr.c_str());
        Serial.print("Température: ");
        Serial.println(tempStr);
        Serial.print("Humidité: ");
        Serial.println(humStr);
      } else {
        Serial.println("Erreur de lecture du capteur DHT22.");
      }
    } else {
      Serial.println("Échec de la lecture du capteur DHT22.");
    }
  }
}
