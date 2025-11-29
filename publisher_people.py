import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)

while True:
    people = random.randint(1, 20)
    msg = f"PeopleCount: {people} - 12114971"
    client.publish("rahaf/people", msg)
    print("Published:", msg)
    time.sleep(3)