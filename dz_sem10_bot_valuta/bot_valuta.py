# Создать бота для вывода текущего курса валют
# (желательно запрос по конкретной валюте)
# /currency USD

import telebot
from sfg import TOKEN
import requests as rq
import xmltodict as xml
from bs4 import BeautifulSoup


bot = telebot.TeleBot(TOKEN)
description = """
Предоставляет информацию о текущем 
курсе валют из Центробанка.
Необходимо сделать запрос в виде
/usd - курс доллара
/eur - курс евро
/cny - курс юаня"""



@bot.message_handler(commands=['start', 'help'])
def bot_description(message):
    bot.send_message(message.chat.id, description)      

@bot.message_handler(content_types=['text'])
def get_currency(message):
    s = rq.get('http://www.cbr.ru/scripts/XML_daily.asp')
    dct = xml.parse(s.text)['ValCurs']['Valute']
    curr = message.text[1:].upper()
    if len(curr) == 3 and message.text[0] == '/':
        for val in dct:
            if val['CharCode'] == curr:
                rate = float(val["Value"].replace(',', '.')) / int(val["Nominal"])
                bot.send_message(message.chat.id,
                                 f'Курс валюты {curr} на текущий день: \n{val["Name"]} - {rate}')
                break
        else:
            bot.reply_to(message, 'Валюта не определена')
    else:
            bot.reply_to(message, 'Неверный ввод.\nСправка - /help')

bot.polling()
