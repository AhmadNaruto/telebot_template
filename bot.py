import telebot
import os
from flask import Flask,request
from pornhub_api import PornhubApi

api = PornhubApi()
def cari(kata):
   tags = random.sample(api.video.tags(kata).tags, 5)
   category = random.choice(api.video.categories().categories)
   return result = api.search.search(ordering="mostviewed", tags=tags, category=category)

#print(result.size())
#for vid in result.videos:
#    print(vid.title, vid.url)


TOKEN = "1171359990:AAFwhEhDSLdCWIFM7lSz0clIUoUTP8erW-w"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Hello! I am bot')

@bot.message_handler(commands=['help']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'Help message')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        h = cari(message.text)
        for co in h.result:
	   bot.reply_to(message, co.url)

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
