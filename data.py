import json, time
import paho.mqtt.client as mqtt

BROKER="broker.hivemq.com"
PORT=1883
TOPIC="cubesat/tle"

payload = {
  "name":"NORBY-3",
  "line1":"1 57179U 23091P   25351.00524733  .00003601  00000-0  19759-3 0  9998",
  "line2":"2 57179  97.5387  43.7336 0016444  40.8093 319.4367 15.14688325136195"
}

c = mqtt.Client()
c.connect(BROKER, PORT, 60)

msg = json.dumps(payload)
c.publish(TOPIC, msg, qos=1, retain=True)
print("Published retained to", TOPIC)
print(msg)

time.sleep(1)
c.disconnect()
