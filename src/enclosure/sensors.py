from mqtt.mqtt_publisher import Publisher_Mqtt
import random

class Sensor(object):
    def __init__(self):
        self.publisher = Publisher_Mqtt()
        
    def publish_message(self, topic, payload):
            self.publisher.client.publish(topic, payload)


class TemperatureSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
    def random(self):
        self.value = random.randint(30,50)
    def send(self):
        self.publish_message("sensors/temperature", self.value)

class HumiditySensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
    def random(self):
        self.value = random.randint(30,50)
    def send(self):
        self.publish_message("sensors/humidity", self.value)

class NoiseSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
    def random(self):
        self.value = random.randint(30,50)
    def send(self):
        self.publish_message("sensors/noise", self.value)


# Testing
a = TemperatureSensor()
print("Generate random data")
a.random()
a.publish_message()