from .sensors import TemperatureSensor, HumiditySensor, FilamentRunOut
from .actuator import Fan, Gate

class Enclosure(object):
    """
    Any enclosure will have a sensors array containing sensors objects. Also,
    it will have an actuators array, containing the actuators object
    """

    def __init__(self, farm, id:int):
        self.id = id
        self.farm = farm
        self.bot = farm.get_bot()

        if isinstance(self, PrinterEnclosure):
            self.enclosure_type = "printerEnclosure"
        elif isinstance(self, FilamentEnclosure):
            self.enclosure_type = "filamentEnclosure"

        self.fan = Fan(self)
        self.gate = Gate(self)
    
    def get_EnclosureId(self):
        return self.id

    def activate_fan(self):
        self.bot.sendMessage(f"ID {self.id}: Activating {self.enclosure_type} fan")
        self.fan.activate()
    
    def deactivate_fan(self):
        self.bot.sendMessage(f"ID {self.id}: Deactivating {self.enclosure_type} fan")
        self.fan.deactivate()

    def open_gate(self):
        self.bot.sendMessage(f"ID {self.id}: Opening {self.enclosure_type} gate")
        self.gate.open()

    def close_gate(self):
        self.bot.sendMessage(f"ID {self.id}: Closing {self.enclosure_type} gate")
        self.gate.close()

    def temperatureNotification(self, value):
        self.bot.sendMessage(f"ID {self.id} : ({self.enclosure_type}) -- Temperature too high. [{value} ºC]")

    def HumidityNotification(self, value):
        self.bot.sendMessage(f"ID {self.id} : ({self.enclosure_type}) -- Humidity too high. [{value} %]")

    def loop_once(self):
        for sensor in self.sensors:
            sensor.random()    # Generate data for every sensor
            sensor.check()     # Check lecture, send it via mqtt and activate/open fan/gate



class PrinterEnclosure(Enclosure):
    def __init__(self, farm, id):
        super().__init__(farm, id)
        self.sensors = [TemperatureSensor(self), HumiditySensor(self)]



class FilamentEnclosure(Enclosure):
    def __init__(self, farm, id):
        super().__init__(farm, id)
        self.sensors = [TemperatureSensor(self), HumiditySensor(self), FilamentRunOut(self)]

    def runOutNotification(self):
        self.bot.sendMessage(f"ID {self.id}: Filament run out")


            
