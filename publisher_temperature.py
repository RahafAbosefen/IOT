import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)

while True:
    msg = "Temperature: 25C - 12114971"
    client.publish("rahaf/temperature", msg)
    print("Published:", msg)
    time.sleep(2)