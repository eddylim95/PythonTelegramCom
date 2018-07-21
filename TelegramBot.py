from datetime import datetime

from telegram.ext import Updater, CommandHandler
from PiCam import PiCam
from Config import config

class TelegramBot:
    def startTelegramBot(self):
        updater = Updater(token=config["telegramApiKey"])
        dispatcher = updater.dispatcher

        try:
            start_CommandHandler = CommandHandler('start', self.__startHandler)
            capture_CommandHandler = CommandHandler('capture', self.__captureHandler)
            stop_CommandHandler = CommandHandler('stop', self.__stopHandler)

            dispatcher.add_handler(start_CommandHandler)
            dispatcher.add_handler(capture_CommandHandler)
            dispatcher.add_handler(stop_CommandHandler)

            updater.start_polling(0.5)
            print("Telegram bot started!")

        except Exception as e:
            print(e)

    def __startHandler(self, bot, update):
        if (update.message.chat_id == int(config['userId'])):
            try:
                time = datetime.now()
                print("Bot online: "+ str(time))
                bot.send_message(chat_id=update.message.chat_id, text="Bot online: "+ str(time))
            except Exception as e:
                print(e)
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Unauthorised")
            print("unauthorised message from " + update.message.chat_id)

    def __captureHandler(self, bot, update):
        if update.message.chat_id == int(config['userId']):
            try:
                bot.send_message(chat_id=update.message.chat_id, text="Capturing...")
                camera = PiCam()
                camera.Snap()
                #subprocess.call("raspistill -o image.jpg")
                bot.sendPhoto(chat_id=update.message.chat_id, photo=open("/home/pi/image.jpg", 'rb'))

            except Exception as e:
                bot.send_message(chat_id=update.message.chat_id, text="Failed to capture")
                print(e)

    def __stopHandler(self, bot, update):
        if update.message.chat_id == int(config['userId']):
            bot.send_message(chat_id=update.message.chat_id, text="Exit terminal")