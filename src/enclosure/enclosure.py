import sys, os
sys.path.append(os.path.dirname(sys.path[0]))

from sensors import TemperatureSensor, HumiditySensor, NoiseSensor, FilamentRunOut
from telegram.telegram import Telegram_Bot

class Enclosure(object):
    """
    Any enclosure will have a sensors array containing sensors objects. Also,
    it will have an actuators array, containing the actuators object
    
    """
    def __init__(self, cfg):
        self.sensors = []
        self.actuators = []

        self.token = cfg["telegram"]["token"]
        self.chatId = cfg["telegram"]["chat_id"]
        self.telegram_bot = Telegram_Bot(self.token)    
        self.bot = Telegram_Bot(self.token).getBot()    # telepot.Bot class

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_actuator(self, actuator):
        self.actuators.append(actuator)

    def check_thresholds(self):
        """
        This function iterates over all the sensors contained in the enclosure, checking its last read and, if needed,
        sends message via telegram
        """
        for sensor in self.sensors:
            msg = sensor.check()
            if msg != "":
                self.bot.sendMessage(self.chatId, sensor.msg)


class FilamentEnclosure(Enclosure):
    def __init__(self):
        Enclosure.__init__(self)
        for sensor in [TemperatureSensor(), HumiditySensor(), FilamentRunOut()]:
            self.add_sensor(sensor)

        ## TO DO: add actuators
