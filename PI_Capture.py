from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from datetime import datetime
import time
#import telegram.ext
from Config import config
import subprocess
from PiCam import Camera

updater = Updater(token= config["telegramApiKey"])
dispatcher = updater.dispatcher
print("Telegram bot started!")

def start(bot, update):
    if (update.message.chat_id == int(config['userId'])):
        try:
            time = datetime.now()
            bot.send_message(chat_id=update.message.chat_id, text="Bot online: "+ str(time))
        except Exception as e:
            print(e)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Unauthorised")
        #bot.send_message(chat_id=update.message.chat_id, text=update.message.chat_id)

def capture(bot, update):
    if (update.message.chat_id == int(config['userId'])):
        try:
            bot.send_message(chat_id=update.message.chat_id, text="Capturing...")
            targetPath = "/home/pi/image.jpg"
            camera = Camera()
            camera.Snap(targetPath)
            #subprocess.call("raspistill -o image.jpg")
            bot.sendPhoto(chat_id=update.message.chat_id, photo=open("/home/pi/image.jpg", 'rb'))
        except Exception as e:
            bot.send_message(chat_id=update.message.chat_id, text="Failed to capture")
            print(e)

def stop(bot, update):
    if (update.message.chat_id == int(config['userId'])):
        bot.send_message(chat_id=update.message.chat_id, text="Exit terminal")

try:
    capture_handler = CommandHandler('capture', capture)
    start_handler = CommandHandler('start', start)
    stop_handler = CommandHandler('stop', stop)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(capture_handler)
    dispatcher.add_handler(stop_handler)
    updater.start_polling(0.5)
except Exception as e:
    print(e)