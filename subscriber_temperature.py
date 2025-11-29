import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Temp Message:", msg.payload.decode())

client = mqtt.Client()
client.on_message = on_message

client.connect("broker.hivemq.com", 1883)
client.subscribe("rahaf/temperature")
client.loop_forever()