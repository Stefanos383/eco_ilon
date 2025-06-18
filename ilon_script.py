import telebot
import random,os

    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("7843358138:AAF1t_EMWMTCgR6xeBlQae7W7NWzqHCCyVs")
@bot.message_handler(commands=["start"])
def start_privet(message):
    bot.reply_to(message,"pruvet")

@bot.message_handler(commands=["random_facts"])
def random_fact(message): 
    facts=["переработка","защищать","повторно использоват","сохранять","сократить количество мусора","спасти животных","заботиться об окружающей среде","использовать экологичные продукты","повышать осведомленность","разумное использование"]
    bot.reply_to(message,random.choice(facts))    

bot.polling()