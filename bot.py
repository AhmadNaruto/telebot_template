import telebot
import os
import pornhub
from flask import Flask,request

TOKEN = "1171359990:AAFwhEhDSLdCWIFM7lSz0clIUoUTP8erW-w"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

search_keywords = []

#client = pornhub.PornHub("5.135.164.72", 3128, search_keywords)
#With proxy, given a Proxy IP and Port. For the countries with restricted access like Turkey, etc.

client = pornhub.PornHub(search_keywords)
def cari(kata):   
    for video in client.getVideos(10,page=2):
    #print(video)
    
    for photo_url in client.getPhotos(5):
    #print(photo_url)
    return video, photo_url

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Hello! I am bot')

@bot.message_handler(commands=['help']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'Help message')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        h = cari(message.text)
	bot.reply_to(message, h)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://ichabottele.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
