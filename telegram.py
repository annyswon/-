import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import re

def get_text(data):
    url = 'https://mai.ru/education/schedule/detail.php?group=М3О-312Б-18'
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    # article = root.select_one('sc-table-row')
    article = root.find_all("div", {"class": "sc-container"})
    reg = '<div class="sc-table-col sc-day-header sc-gray">{}'.format(data)
    for art in article:
        if re.findall(reg, str(art)):
            res = re.findall(r'<span class="sc-title">[\W+\D+]+n>', str(art))

    datares = []
    for r in res:
        resAll = r[23:]
        datares.append(resAll.replace("</span>", ""))
    return datares

bot = telebot.TeleBot('1132941408:AAHfZStCTNIxj4-RwCMpcv52dJE5YC2h6sI');

#  python telegram.py

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text_count = len(message.text)
    if message.text == "/rasp":
        bot.send_message(message.from_user.id, "Назовите дату")
    elif text_count == 5:
        res = get_text(str(message.text))
        for r in res:
            bot.send_message(message.from_user.id, r)
    elif message.text == "/audit":
        bot.send_message(message.from_user.id, "Скажите номер аудитории")
        bot.send_message(message.from_user.id, "Скажите дату")
    else:
        bot.send_message(message.from_user.id, "команда с ошибкой")


bot.polling(none_stop=True, interval=0)

