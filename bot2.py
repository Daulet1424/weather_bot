import telebot
from telebot import types


bot = telebot.TeleBot('6253766259:AAEfxrASAV64LVLylvalySGHUISFBghBJlI')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b> <u><b>{message.from_user.last_name}</b></u>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['website'])
def bot_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетите сайт", url='https://brainius.kz/'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands=['help'])
def bot_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)
    if website == True:
        bot.send_message(message.chat.id, 'Формулы', url = 'https://brainius.kz/')
bot.polling(none_stop=True)



