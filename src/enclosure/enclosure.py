import sys, os
sys.path.append(os.path.dirname(sys.path[0]))

from .sensors import TemperatureSensor, HumiditySensor, FilamentRunOut
from .actuator import Fan, Gates
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

        self.fan = Fan(self.id)
        self.gates = Gates(self.id)

    
    def send_header(self):
        self.bot.sendMessage(f"---------- PRINTER {self.id} ----------")
        self.notSentHeader = False


    def loop_once(self):
        self.notSentHeader = True

        for sensor in self.sensors:
            sensor.random()    # Generate data for every sensor
            sensor.check()     # 

        if self.temperature.msg == "Temperature too high. ":
            if self.notSentHeader:
                self.bot.sendMessage(f"---------- PRINTER {self.id} ----------")
                self.notSentHeader = False

            self.bot.sendMessage(f"{self.temperature.msg} [{self.temperature.lecture} ºC]")
            self.fan.activate()
            self.bot.sendMessage(self.fan.msg)

        if self.humidity.msg== "Humidity too high. ":
            if self.notSentHeader:
                self.bot.sendMessage(f"---------- PRINTER {self.id} ----------")
                self.notSentHeader = False

            self.bot.sendMessage(f"{self.humidity.msg} [{self.humidity.lecture} %]")
            self.gates.activate()
            self.bot.sendMessage(self.gates.msg)



class FilamentEnclosure(object):
    def __init__(self, id, bot):
        self.id = id
        self.bot = bot
        
        self.temperature = TemperatureSensor(self.id)
        self.humidity = HumiditySensor(self.id)
        self.filament = FilamentRunOut(self.id)

        self.sensors = [self.temperature, self.humidity, self.filament]

        self.fan = Fan(self.id, isFilament = True)
        self.gates = Gates(self.id, isFilament = True) 

    def send_header(self):
        self.bot.sendMessage(f"---------- PRINTER {self.id} (filament) ----------")
        self.notSentHeader = False

    def loop_once(self):
        self.notSentHeader = True

        for sensor in self.sensors:
            sensor.random()    # Generate data for every sensor
            sensor.check()     # 

        if self.temperature.msg == "Temperature too high. ":
            if self.notSentHeader:
                self.send_header()

            self.bot.sendMessage(f"Filament: {self.temperature.msg} [{self.temperature.lecture} ºC]")
            self.fan.activate()
            self.bot.sendMessage(self.fan.msg)

        if self.humidity.msg== "Humidity too high. ":
            if self.notSentHeader:
                self.bot.sendMessage(f"---------- PRINTER {self.id} (filament) ----------")
                self.notSentHeader = False

            self.bot.sendMessage(f"Filament: {self.humidity.msg} [{self.humidity.lecture} %]")
            self.gates.activate()
            self.bot.sendMessage(self.gates.msg)

        if self.filament.msg == "FILAMENT RUN OUT":
            if self.notSentHeader:
                self.bot.sendMessage(f"---------- PRINTER {self.id} (filament) ----------")
                self.notSentHeader = False

            self.bot.sendMessage(f"Filament: {self.filament.msg}")
            
