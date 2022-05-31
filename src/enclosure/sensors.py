import sys, os
sys.path.append(os.path.dirname(sys.path[0]))

from mqtt.mqtt_publisher import Publisher_Mqtt
import random

class Sensor(object):
    def __init__(self):
        self.publisher = Publisher_Mqtt()
        self.value = ""
        self.msg = ""
        self.payload = {"value":self.value, "msg":self.msg}
        
    def publish_message(self, topic, payload):
        """ Publish payload to an specific topic

        Args:
            topic (str): EX: sensors/humidity
            payload (_type_): Data to be sent. Lectures of the sensor
        """        
        self.publisher.client.publish(topic, payload)


class TemperatureSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        
    def random(self):
        """Generete random data simulating sensor lecture"""
        self.value = random.randint(30,50)

    def send(self):
        """Send last lecture of the sensor to the broker via mqtt"""
        self.publish_message("sensors/temperature", self.payload)

    def check(self):
        if self.value > 45:
            self.msg = "Temperature too high. Opening the fan..."
            self.send()
        elif self.value > 40:
            self.msg = "Temperature is high, Do you want to open the fan?"
            self.send()
        else:
            pass

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

class FilamentRunOut(Sensor):
    def __init__(self):
        Sensor.__init__(self)
    def random(self):
        self.value = random.randint(30,50)
    def send(self):
        self.publish_message("sensors/FilamentRunOut", self.value)


