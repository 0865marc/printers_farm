from telegram.telegram import Telegram_Bot
from enclosure.enclosure import PrinterEnclosure, FilamentEnclosure
import time

class Farm(object):

    def __init__(self, cfg):
        self.cfg = cfg
        self.token = cfg["telegram"]["token"]
        self.chatId = cfg["telegram"]["chat_id"]
        self.bot = Telegram_Bot(self)
        self.printers = dict()
        
        # farm.printers = {
        # {printer_id}:{"Printer":PrinterEnclosure Object, "Filament":FilamentEnclosure Object},
        # {printer_id}:{"Printer":PrinterEnclosure Object, "Filament":FilamentEnclosure Object},
        # {printer_id}:{"Printer":PrinterEnclosure Object, "Filament":FilamentEnclosure Object}
        # }

    def get_bot(self):
        return self.bot

    def get_printers(self):
        return self.printers

    def add_printer(self, id:int):
        """ This function adds a new printer to the farm.printers dictionary.
            
        Args:
            id (int): ID of the new printer to be added.
        """        

        if id not in self.printers:
            self.printers[id] = {"Printer":PrinterEnclosure(self, id), "Filament":FilamentEnclosure(self, id)}
        else:
            self.bot.sendMessage("Error, printer id already registered. Type /printers to see all the printers")

    def printers_list(self):
        """ 
        This function list all existing printers in farm.printers dictionary via telegram message.
        """     

        printer_list = "---------- PRINTER LIST ----------\n"
        if len(self.printers) == 0:
            printer_list += "No printers registered yet, add one with /add_printer <printer_id>"
        for printer_id in self.printers:
            printer_list += f"\t Printer {printer_id}\n"

        self.bot.sendMessage(printer_list)


    def start(self):
        """
        This function starts the farm with no printers. You have to add new printers via telegram /add_printer <printer_id>.
        Once you have added printers, it generates random data and simulates real printers each <timer> seconds, 
        which you can specify in the config.yaml file. (Default: each 10 seconds)
        """        
        while True:
            for printer_id in self.printers:                            # For every printer in the farm.printers dictionary
                self.printers[printer_id]["Printer"].loop_once()        # Generate new data and simulate PrinterEnclosure
                self.printers[printer_id]["Filament"].loop_once()       # Generate new data and simulate FilamentEnclosure

            time.sleep(self.cfg["farm"]["timer"])


