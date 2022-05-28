import paho.mqtt.client as mqtt         # https://github.com/eclipse/paho.mqtt.python#client

# First, you have to run the mosquitto broker --->   mosquitto -c mosquitto.conf

class Subscriber_Mqtt():
    def __init__(self) -> None:
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect("localhost")
        self.client.subscribe("sensors/#") 
        self.client.loop_forever()


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        #self.client.subscribe("$SYS/#")    

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        if msg.topic == "sensors/temperature":
            print(msg.topic+" "+str(msg.payload))
        elif msg.topic == "sensors/humidity":
            print(msg.topic+" "+str(msg.payload))
        else:
            print(msg.topic+" "+str(msg.payload))
            print("Unknown topic")

        

test = Subscriber_Mqtt()


