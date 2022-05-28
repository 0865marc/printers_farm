from email import message
import telepot                                       # https://telepot.readthedocs.io/en/latest/
from telepot.loop import MessageLoop
import time

BOT_TOKEN = "5529655394:AAGN9hGkbrhcVYvq_EWYQzag4P5Y7q56DBs"

class Bot(object):

    def __init__(self, token):
        self.bot = telepot.Bot(BOT_TOKEN)
        MessageLoop(self.bot, self.handle).run_as_thread()
        print("Listening......")
        while True:
            time.sleep(10)

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type == "text":
            command = msg["text"]
            print("Command recieved: ", command)

            if command == "/something":
                pass
            elif command == "/somethingDifferent":
                pass
            else:
                print("Unknown command")



if __name__ == "__main__":
    farm_Bot = Bot(BOT_TOKEN)