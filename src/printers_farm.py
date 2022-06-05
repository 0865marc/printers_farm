from telegram.telegram import Telegram_Bot
from enclosure.enclosure import Enclosure, FilamentEnclosure
import time

class Farm(object):

    def __init__(self):
        self.token = "5529655394:AAGN9hGkbrhcVYvq_EWYQzag4P5Y7q56DBs"
        self.chatId = "286104504"
        self.bot = Telegram_Bot(self.token, self.chatId)

    def start(self):
        printers = {1: [Enclosure(1, self.bot), FilamentEnclosure(1, self.bot)]}

        while True:
            for printer_id in printers:
                printers[printer_id][0].loop_once()
                printers[printer_id][1].loop_once()

            time.sleep(10)



from enclosure.enclosure import Enclosure, FilamentEnclosure
#a = Enclosure(1)
#a.loop()


a = Farm()
a.start()