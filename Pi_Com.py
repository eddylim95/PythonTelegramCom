import telepot
from pprint import pprint
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup
import Config

class MessageHandler():
    __bot = telepot.Bot(Config.config['apiKey'])
    print(__bot.getMe())
    __userId = 264234098

    def start(self):
        MessageHandler.__bot.sendMessage(MessageHandler.__userId, "Pi online, ready to receive messages")
        MessageLoop(MessageHandler.__bot, MessageHandler.__handle).run_forever()

    def __handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        pprint(msg)
        print(content_type, chat_type, chat_id)


msghandler = MessageHandler()
msghandler.start()
