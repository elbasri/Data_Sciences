//Include Libs
#include <DHT11.h>

DHT11 dht11(2);

void setup() {
  Serial.begin(9600);
}
void loop() {
  //wait  for 2 second
  delay(2000);
  //get DHT data
  float temperature = dht11.readTemperature();
  delay(500); // Required to get both readings consecutively
  float humidity = dht11.readHumidity();

  String dhtData = String(humidity) + "," + String(temperature);
  Serial.println(dhtData);
  return dhtData;
}
