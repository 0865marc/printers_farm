import paho.mqtt.client as mqtt         # https://github.com/eclipse/paho.mqtt.python#client

# First, you have to run the mosquitto broker --->   mosquitto -c mosquitto.conf

class Publisher_Mqtt(object):
    def __init__(self) -> None:
        self.client = mqtt.Client()
        self.code = 0
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_publish

        self.client.connect("localhost")


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.client.subscribe("$SYS/#")

        self.code = 1

    # The callback for when a message that was to be sent using the publish() call has completed transmission to the broker
    def on_publish(self, client, userdata, msg):
        pass



        
