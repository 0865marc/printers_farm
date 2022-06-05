import sys, os
sys.path.append(os.path.dirname(sys.path[0]))

from .sensors import TemperatureSensor, HumiditySensor, FilamentRunOut
from telegram.telegram import Telegram_Bot

class Enclosure(object):
    """
    Any enclosure will have a sensors array containing sensors objects. Also,
    it will have an actuators array, containing the actuators object
    """

    def __init__(self, id, bot):
        self.id = id
        self.bot = bot
        
        self.temperature = TemperatureSensor(self.id)
        self.humidity = HumiditySensor(self.id)

        self.sensors = [self.temperature, self.humidity]
        self.actuators = [] 
    

    def loop_once(self):
        for sensor in self.sensors:
            sensor.random()    # Generate data for every sensor
            sensor.check()     # 

        if self.temperature.msg == "Temperature too high. Opening the fan...":
            self.bot.sendMessage(f"-- PRINTER {self.id}: {self.temperature.msg}")
            # ACTUATOR

        if self.humidity.msg== "Humidity too high. Opening the fan...":
            self.bot.sendMessage(f"-- PRINTER {self.id}: {self.humidity.msg}")
            # ACTUATOR


class FilamentEnclosure(object):
    def __init__(self, id, bot):
        self.id = id
        self.bot = bot
        
        self.temperature = TemperatureSensor(self.id)
        self.humidity = HumiditySensor(self.id)
        self.filament = FilamentRunOut(self.id)

        self.sensors = [self.temperature, self.humidity, self.filament]
        self.actuators = [] 

    def loop_once(self):
        for sensor in self.sensors:
            sensor.random()    # Generate data for every sensor
            sensor.check()     # 

        if self.temperature.msg == "Temperature too high. Opening the fan...":
            self.bot.sendMessage(f"-- PRINTER{self.id} (filament): {self.temperature.msg}")
            # ACTUATOR

        if self.humidity.msg== "Humidity too high. Opening the fan...":
            self.bot.sendMessage(f"-- PRINTER {self.id} (filament): {self.humidity.msg}")
            # ACTUATOR

        if self.filament.msg == "FILAMENT RUN OUT":
            self.bot.sendMessage(f"-- PRINTER {self.id} (filament): {self.humidity.msg}")
            pass
