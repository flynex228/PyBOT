import telebot
import random
import string
from telebot import types

def gstring(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string

def catalog_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    id = types.KeyboardButton(text="/id")
    name = types.KeyboardButton(text="/name")
    help = types.KeyboardButton(text="Помощь")
    photo = types.KeyboardButton(text="/photo")
    rmd = types.KeyboardButton(text="/rmd")
    keyboard.add(id, name, help, photo, rmd)
    return keyboard
    


bot = telebot.TeleBot("1757067302:AAGbJbtBqrbtJIz2Oj8F_lfkSpyOsSTc8rY")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "/start":
           bot.send_message(message.chat.id, "Привет, я бот, который поможет тебе найти информацию!", reply_markup=catalog_keyboard())
    elif message.text == "/id":
        bot.reply_to(message, message.chat.id)
    elif message.text == "/name":
        bot.reply_to(message, message.chat.first_name)
    elif message.text == "Помощь" or message.text == "помощь":
        bot.reply_to(message, "Выбери команду\n/id\n/name\n/start\n/photo\n/rmd\n")
    elif message.text == "/photo":
         A=random.randint(1,2)
         if A==1:
         	bot.send_photo(message.chat.id,"https://images.app.goo.gl/5Ed89FtevfE3ecvd7")
         elif A==2:
         	bot.send_photo(message.chat.id,"https://images.app.goo.gl/oa9NJJr9XJXJMGzt6")
    elif message.text == "/rmd":
        bot.send_message(message.chat.id, "Пожалуйста подождите...")
        c = 0
        while True:
            if c>=30:
                bot.send_message(message.chat.id, "Превышено время поиска попробуйте ещё раз!")
                c = 0
                break
            try:
                bot.send_photo(message.chat.id, "https://clck.ru/"+gstring(5))
                break
            except:
                try:
                    bot.send_photo(message.chat.id, "https://goo.su/"+gstring(4))
                    break
                except:
                    try:
                        bot.send_photo(message.chat.id, "https://goo-gl.ru/"+gstring(5))
                        break
                    except:
                        try:
                            bot.send_photo(message.chat.id, "https://vk.cc/"+gstring(6))
                            break
                        except:
                            try:
                                bot.send_photo(message.chat.id, "https://ssilka.su/"+gstring(5))
                                break
                            except:{}
            c+=1
    else:bot.reply_to(message, "Прости,я тебя не понимаю:(")
        
                    
                
        

bot.polling()
