import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)

while True:
    msg = "Humidity: 60% - 12114971"
    client.publish("rahaf/humidity", msg)
    print("Published:", msg)
    time.sleep(2)