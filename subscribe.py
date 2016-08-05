import sys
import paho.mqtt.client as mqtt

args = sys.argv
if len(args) <= 1:
    print("The argv should be host, port and topic")
    sys.exit()

host = args[1]
port = args[2]
topic = args[3]

def on_connect(mosq, obj, rc):
    mqttc.subscribe(topic, 0)

def on_message(mosq, obj, msg):
    global message
    print(str(msg.payload))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed to : " + str(topic))

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(host, port, 60)

# Continue the network loop
mqttc.loop_forever()
