/*
  ReadMultipleFields
  
  Description: Demonstates reading from a public channel which requires no API key (reading from a private channel requires a read API key).
               The values read from the public channel is the current wind direction, wind speed, humidity, outside temperature, rain, pressure, 
               power level, and light intensity  at MathWorks headquaters in Natick, MA.The functionality also provides us to read the 
               status message, location coordinates, and created-at timestamp associated with the latest feed.
  
  Hardware: ESP32 based boards
  
  !!! IMPORTANT - Modify the secrets.h file for this project with your network connection and ThingSpeak channel details. !!!
  
  Note:
  - Requires installation of EPS32 core. See https://github.com/espressif/arduino-esp32/blob/master/docs/arduino-ide/boards_manager.md for details. 
  - Select the target hardware from the Tools->Board menu
  - This example is written for a network using WPA encryption. For WEP or WPA, change the WiFi.begin() call accordingly.
  
  ThingSpeak ( https://www.thingspeak.com ) is an analytic IoT platform service that allows you to aggregate, visualize, and 
  analyze live data streams in the cloud. Visit https://www.thingspeak.com to sign up for a free account and create a channel.  
  
  Documentation for the ThingSpeak Communication Library for Arduino is in the README.md folder where the library was installed.
  See https://www.mathworks.com/help/thingspeak/index.html for the full ThingSpeak documentation.
  
  For licensing information, see the accompanying license file.
  
  Copyright 2020, The MathWorks, Inc.
*/

#include <WiFi.h>
//#include <secrets.h>
#include <ThingSpeak.h> // always include thingspeak header file after other header files and custom macros


#define SECRET_SSID "NacerWifi"      // replace with your WiFi network name
#define SECRET_PASS "NCR"            // replace with your WiFi password
#define SECRET_CH_ID_WEATHER_STATION 12397 // MathWorks weather station
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
WiFiClient client;

// Weather station channel details
unsigned long weatherStationChannelNumber = SECRET_CH_ID_WEATHER_STATION;

int statusCode = 0;
int field[8] = {1, 2, 3, 4, 5, 6, 7, 8};

void setup() {
  Serial.begin(115200); // Initialize serial
  while (!Serial) {
    ; // wait for the serial port to connect
  }

  ThingSpeak.begin(client); // Initialize ThingSpeak
}

void loop() {
  statusCode = ThingSpeak.readMultipleFields(weatherStationChannelNumber);

  if (statusCode == 200) {
    // Fetch the stored data
    int windDir = ThingSpeak.getFieldAsInt(field[0]);
    float windSpeed = ThingSpeak.getFieldAsFloat(field[1]);
    int percentHumid = ThingSpeak.getFieldAsInt(field[2]);
    float tempInF = ThingSpeak.getFieldAsFloat(field[3]);
    float rainInchPerMin = ThingSpeak.getFieldAsFloat(field[4]);
    float pressureInHg = ThingSpeak.getFieldAsFloat(field[5]);
    float powerLevel = ThingSpeak.getFieldAsFloat(field[6]);
    int lightIntensity = ThingSpeak.getFieldAsInt(field[7]);

    Serial.println("Wind Direction (North = 0 degrees): " + String(windDir));
    Serial.println("Wind Speed (mph): " + String(windSpeed));
    Serial.println("% Humidity: " + String(percentHumid));
    Serial.println("Temperature (F): " + String(tempInF));
    Serial.println("Rain (Inches/minute): " + String(rainInchPerMin));
    Serial.println("Pressure (\Hg): " + String(pressureInHg));
    Serial.println("Power Level (V): " + String(powerLevel));
    Serial.println("Light Intensity: " + String(lightIntensity));
  } else {
    Serial.println("Problem reading channel. HTTP error code " + String(statusCode));
  }

  delay(5000); // no need to fetch too often
}