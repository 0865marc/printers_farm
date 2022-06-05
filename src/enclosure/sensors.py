import sys, os
sys.path.append(os.path.dirname(sys.path[0]))

from mqtt.mqtt_publisher import Publisher_Mqtt
import random

class Sensor(object):
    def __init__(self, enclosure):
        self.publisher = Publisher_Mqtt()
        self.lecture = 99999
        self.enclosure = enclosure
        
    def publish_message(self, topic, value): 
        self.publisher.client.publish(topic, value)     #PUBLISH LECTURE VIA MQTT


class TemperatureSensor(Sensor):
    def __init__(self, enclosure):
        super().__init__(enclosure)
        
    def random(self):
        """Generate random data simulating sensor lecture"""
        self.lecture = random.randint(20,50)

    def send(self):
        """Send last lecture and message of the sensor to the broker via mqtt"""
        self.publish_message(f"sensors/{self.enclosure.get_EnclosureId()}/temperature", self.lecture)

    def check(self):
        if self.lecture > 45:
            # High lecture
            if self.publisher.code == 1:                # If successfully conected to the broker
                self.send()                             # Send the lecture via MQTT
            
            self.enclosure.temperatureNotification(self.lecture)
            self.enclosure.activate_fan()

        elif self.lecture >= 20:
            # Normal lecture
            if self.publisher.code == 1:                # If successfully conected to the broker
                self.send()                             # Send the lecture via MQTT           
        else:
            # Error with the lecture
            self.lecture = 99999     
            if self.publisher.code == 1:                # If successfully conected to the broker
                self.send()                             # Send the lecture via MQTT


class HumiditySensor(Sensor):
    def __init__(self, enclosure):
        super().__init__(enclosure)
    def random(self):
        """Generate random data simulating sensor lecture"""
        self.lecture = random.randint(0,100)
    def send(self):
        """Send last lecture and message of the sensor to the broker via mqtt"""
        self.publish_message(f"sensors/{self.enclosure.get_EnclosureId()}/humidity", self.lecture)

    def check(self):
        if self.lecture > 90:
            # High lecture
            if self.publisher.code == 1:                # If successfully conected to the broker
                self.send()                             # Send the lecture via MQTT
            self.enclosure.HumidityNotification(self.lecture)
            self.enclosure.open_gate()

        elif self.lecture >= 0:
            # Normal lecture
            if self.publisher.code == 1:                # If successfully conected to the broker
                self.send()                             # Send the lecture via MQTT  
        else:
            # Error with the lecture
            self.lecture = 99999
            if self.publisher.code == 1:                # If successfully conected to the broker
                self.send()                             # Send the lecture via MQTT



class FilamentRunOut(Sensor):
    def __init__(self, enclosure):
        super().__init__(enclosure)
        
    def random(self):
        """Generate random data simulating sensor lecture"""
        self.lecture = random.randint(0, 100)
        if self.lecture >= 95:
            self.lecture = "FILAMENT RUN OUT"
        else:
            self.lecture = "FILAMENT OK!"

    def send(self):
        """Send last lecture and message of the sensor to the broker via mqtt"""
        self.publish_message(f"sensors/{self.enclosure.get_EnclosureId}/temperature/lecture", self.lecture)

    def check(self):
        if self.lecture == "FILAMENT RUN OUT":
            if self.publisher.code == 1:                # If successfully conected to the broker
                self.send()                             # Send the lecture via MQTT
            self.enclosure.runOutNotification()
            
        elif self.lecture == "FILAMENT OK!":
            if self.publisher.code == 1:                # If successfully conected to the broker
                self.send()                             # Send the lecture via MQTT
        else:
            self.lecture = 99999
            if self.publisher.code == 1:                # If successfully conected to the broker
                self.send()                             # Send the lecture via MQTT


