#export INFLUXDB_TOKEN=PI0oop3XqXjTYarUdhrQgg5D1SapnTGifGZX0c0yjd8qMf988lhUUjZpnQDmUmYE9zX9apHN7knR9iLn0KlPcA==
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from random import randint

token = "PI0oop3XqXjTYarUdhrQgg5D1SapnTGifGZX0c0yjd8qMf988lhUUjZpnQDmUmYE9zX9apHN7knR9iLn0KlPcA=="
org = "nacer"
url = "http://94.130.23.31:7086"


#initiate connection
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

print(client)

bucket="nacerbucket"


#send data
write_api = client.write_api(write_options=SYNCHRONOUS)
   
for value in range(500):
  Temperature = randint(5,20)
  Humidite = randint(30,80)
  point = (
    Point("sensorData")
    .tag("tagname1", "TempHum")
    .field("Temperature", Temperature)
    .field("Humidite", Humidite)
  )
  write_api.write(bucket=bucket, org="nacer", record=point)
  time.sleep(1) # separate points by 1 second


#get data
query_api = client.query_api()

query = """from(bucket: "nacerbucket")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "sensorData")"""
tables = query_api.query(query, org="nacer")

for table in tables:
  for record in table.records:
    print(record)


#agrega

query_api = client.query_api()

query = """from(bucket: "nacerbucket")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "sensorData")
  |> mean()"""
tables = query_api.query(query, org="nacer")

for table in tables:
    for record in table.records:
        print(record)