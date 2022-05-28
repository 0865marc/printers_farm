from mqtt.mqtt_publisher import Publisher_Mqtt


class Sensor(object):
    def __init__(self):
        self.publisher = Publisher_Mqtt()
        

    def publish_message(self):
        if isinstance(self, SensorTemperatura):
            self.publisher.client.publish("sensors/temperature", self.value)


class SensorTemperatura(Sensor):
    def __init__(self):
        Sensor.__init__(self)

    def random(self):
        self.value = 32


# Testing
a = SensorTemperatura()
print("Generate random data")
a.random()
a.publish_message()