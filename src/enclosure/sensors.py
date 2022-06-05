import sys, os
sys.path.append(os.path.dirname(sys.path[0]))

from mqtt.mqtt_publisher import Publisher_Mqtt
import random

class Sensor(object):
    def __init__(self):
        self.publisher = Publisher_Mqtt()
        self.lecture = 99999
        
    def publish_message(self, topic, value): 
        self.publisher.client.publish(topic, value)     #PUBLISH LECTURE VIA MQTT


class TemperatureSensor(Sensor):
    def __init__(self, enclosure_id):
        Sensor.__init__(self)
        self.enclosure_id = enclosure_id
        
    def random(self):
        """Generate random data simulating sensor lecture"""
        self.lecture = random.randint(30,50)

    def send(self):
        """Send last lecture and message of the sensor to the broker via mqtt"""
        self.publish_message(f"sensors/{self.enclosure_id}/temperature/lecture", self.lecture)

    def check(self):
        if self.lecture > 45:
            self.msg = "Temperature too high. Opening the fan..."
            self.send()

        elif self.lecture >= 30:
            self.msg = "Temperature OK"
            self.send()
        else:
            self.msg = "Error with the lecture of the sensor"
            self.lecture = 99999
            self.send()

class HumiditySensor(Sensor):
    def __init__(self, enclosure_id):
        Sensor.__init__(self)
        self.enclosure_id = enclosure_id
        
    def random(self):
        """Generate random data simulating sensor lecture"""
        self.lecture = random.randint(0,100)

    def send(self):
        """Send last lecture and message of the sensor to the broker via mqtt"""
        self.publish_message(f"sensors/{self.enclosure_id}/temperature/lecture", self.lecture)

    def check(self):
        if self.lecture > 80:
            self.msg = "Humidity too high. Opening the fan..."
            self.send()
        elif self.lecture >= 0:
            self.msg = "Temperature OK"
            self.send()
        else:
            self.msg = "Error with the lecture of the sensor"
            self.lecture = 99999
            self.send()

class FilamentRunOut(Sensor):
    def __init__(self, enclosure_id):
        Sensor.__init__(self)
        self.enclosure_id = enclosure_id
        
    def random(self):
        """Generate random data simulating sensor lecture"""
        self.lecture = random.randint(0, 100)
        if self.lecture >= 95:
            self.lecture = "FILAMENT RUN OUT"
        else:
            self.lecture = "FILAMENT OK!"

    def send(self):
        """Send last lecture and message of the sensor to the broker via mqtt"""
        self.publish_message(f"sensors/{self.enclosure_id}/temperature/lecture", self.lecture)

    def check(self):
        if self.lecture == "FILAMENT RUN OUT":
            self.msg = "Temperature too high. Opening the fan..."
            self.send()
        elif self.lecture == "FILAMENT OK!":
            self.msg = "Temperature OK"
            self.send()
        else:
            self.msg = "Error with the lecture of the sensor"
            self.lecture = 99999
            self.send()


