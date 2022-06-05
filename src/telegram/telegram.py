import telepot                                       # https://telepot.readthedocs.io/en/latest/
from telepot.loop import MessageLoop

class Telegram_Bot(object):

    def __init__(self, farm):
        self.bot = telepot.Bot(farm.token)
        self.chatId = farm.chatId
        self.farm = farm
        MessageLoop(self.bot, self.handle).run_as_thread()
        print("BOT STARTED")

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type == "text":
            command = msg["text"]
            print(f"Command recieved {chat_id}: ", command)
            command = command.split(" ")

            if command[0].upper() == "/add_printer".upper():   # /add_printer <printer_id>
                if len(command) == 2:
                    if command[1].isnumeric():
                        self.farm.add_printer(int(command[1]))
                    else:
                        self.farm.bot.sendMessage("Error, printer id MUST be numeric")
                else:
                    self.farm.bot.sendMessage("Error, ID is not valid")

            elif command[0].upper() == "/printers_list".upper():     # /printers_list
                self.farm.printers_list()
            
            elif command[0].upper() == "/activate".upper():        # /activate <fan or gate> <printer_id> <enclosure or filament>
                printer_id = int(command[2])

                if printer_id in self.farm.printers.keys():
                    if command[3].upper() == "printer".upper():
                        enclosure_destination = "Printer"
                    elif command[3].upper() == "filament".upper():
                        enclosure_destination = "Filament"
                    else:
                        enclosure_destination = "Error"
                        self.farm.bot.sendMessage("Error, must be Enclosure OR Filament")

                    if enclosure_destination != "Error":
                        if command[1].upper() == "fan".upper():
                            self.farm.printers[printer_id][enclosure_destination].fan.activate()
                            self.farm.bot.sendMessage(f"{enclosure_destination} {printer_id}: Fan activated")
                        elif command[1].upper() == "gate".upper():
                            self.farm.printers[printer_id][enclosure_destination].gate.activate()
                            self.farm.bot.sendMessage(f"{enclosure_destination} {printer_id}: Fan deactivated")
                        else:
                            self.farm.bot.sendMessage("Error, actuator must be <fan OR gate>")
                else:
                    self.farm.bot.sendMessage("Printer does not exist")
            
            elif command[0] == "/help" or "/start":
                if command[0] == "/start":
                    self.farm.bot.sendMessage("Welcome to Printers_farm bot")
                self.farm.bot.sendMessage("\t ----- HELP -----\n")
                self.farm.bot.sendMessage("\t /add_printer <printer_id> to add a new printer\n")
                self.farm.bot.sendMessage("\t /printers_list to see all printers registered\n")
                self.farm.bot.sendMessage("\t /activate <fan or gate> <printer_id> <printer or filament>\n")

            else:
                self.farm.bot.sendMessage("Unknown command, use /help to get more info")

    def sendMessage(self, msg):
        self.bot.sendMessage(self.chatId, msg)
