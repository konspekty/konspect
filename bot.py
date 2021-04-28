import telebot
bot = telebot.TeleBot('1717190330:AAFFPo5lELyAVeyVCTDShGlx82NQHZ-mm6s')
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Пошел нахуй, {message.from_user.first_name}')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Миша пидр!')
    else:
        bot.send_message(message.from_user.id, 'Пиши нормально еблан.')
   
        
bot.polling(none_stop=True)
