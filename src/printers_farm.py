from telegram.telegram import Telegram_Bot
from enclosure.enclosure import PrinterEnclosure, FilamentEnclosure
import time

class Farm(object):

    def __init__(self):
        self.token = "5529655394:AAGN9hGkbrhcVYvq_EWYQzag4P5Y7q56DBs"
        self.chatId = "286104504"
        self.bot = Telegram_Bot(self)
        self.printers = dict()

    def get_bot(self):
        return self.bot

    def get_printers(self):
        return self.printers

    def add_printer(self, id):
        if id not in self.printers:
            self.printers[id] = {"Printer_Enclosure":PrinterEnclosure(self, id), "Filament":FilamentEnclosure(self, id)}
        else:
            self.bot.sendMessage("Error, printer id already registered. Type /printers to see all the printers")

    def printers_list(self):
        printer_list = "---------- PRINTER LIST ----------\n"
        if len(self.printers) == 0:
            printer_list += "No printers registered yet, add one with /add_printer <printer_id>"
        for printer_id in self.printers:
            printer_list += f"\t Printer {printer_id}\n"

        self.bot.sendMessage(printer_list)


    def start(self):
        while True:
            for printer_id in self.printers:
                self.printers[printer_id]["Printer_Enclosure"].loop_once()
                self.printers[printer_id]["Filament"].loop_once()

            time.sleep(10)



a = Farm()
a.start()

