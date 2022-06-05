from email import message
import telepot                                       # https://telepot.readthedocs.io/en/latest/
from telepot.loop import MessageLoop
import time

#TO DO: cfg file
BOT_TOKEN = "5529655394:AAGN9hGkbrhcVYvq_EWYQzag4P5Y7q56DBs"

class Telegram_Bot(object):

    def __init__(self, token, chatId):
        self.bot = telepot.Bot(token)
        self.chatId = chatId
        MessageLoop(self.bot, self.handle).run_as_thread()
        print("Listening......")

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type == "text":
            command = msg["text"]
            print(f"Command recieved {chat_id}: ", command)

            if command == "/something":
                pass
            elif command == "/somethingDifferent":
                pass
            else:
                print("Unknown command")
    
    def getBot(self):
        return self.bot

    def sendMessage(self, msg):
        self.bot.sendMessage(self.chatId, msg)




if __name__ == "__main__":
    farm_Bot = Telegram_Bot(BOT_TOKEN)
    while True:
        time.sleep(51)