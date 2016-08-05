import sys
import paho.mqtt.client as mqtt

args = sys.argv
if len(args) <= 1:
    print("The argv should be host, port, topic and payload")
    sys.exit()

host = args[1]
port = args[2]
topic = args[3]
payload = args[4]

def on_connect(mosq, obj, rc):
    print("Connected")

def on_publish(client, userdata, mid):
    print("published")

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# Connect
mqttc.connect(host, port, 60)
mqttc.publish(topic, payload, 0)

# Continue the network loop
# mqttc.loop_forever()
