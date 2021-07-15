import telebot
import random
import string
from telebot import types

def gstring(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string

def win():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    id = types.KeyboardButton(text="you WIN")
    keyboard.add(id)
    return keyboard

def catalog_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    id = types.KeyboardButton(text="/id")
    name = types.KeyboardButton(text="/name")
    help = types.KeyboardButton(text="Помощь")
    photo = types.KeyboardButton(text="/photo")
    rmd = types.KeyboardButton(text="/rmd")
    keyboard.add(id, name, help, photo, rmd)
    return keyboard
def catalog_keyboard2():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    id = types.KeyboardButton(text="1")
    name = types.KeyboardButton(text="2")
    help = types.KeyboardButton(text="3")
    photo = types.KeyboardButton(text="4")
    rmd = types.KeyboardButton(text="5")
    hi = types.KeyboardButton(text="6")
    hi1 = types.KeyboardButton(text="7")
    hi2 = types.KeyboardButton(text="8")
    hi3 = types.KeyboardButton(text="9")
    hi4 = types.KeyboardButton(text="0")
    keyboard.row(id, name, help)
    keyboard.row(photo, rmd, hi)
    keyboard.row(hi1, hi2, hi3)
    keyboard.row(hi4)
   
    return keyboard


bot = telebot.TeleBot("BOT_KEY")
lv = 0

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global lv
    if message.text == "/start":
           bot.send_message(message.chat.id, "Привет, я бот, который поможет тебе найти информацию!", reply_markup=catalog_keyboard())
    elif message.text == "/id":
        bot.reply_to(message, message.chat.id)
    elif message.text == "/cod":
        bot.reply_to(message, "Введите пароль", reply_markup=catalog_keyboard2())
    elif message.text == "/name":
        bot.reply_to(message, message.chat.first_name)
    elif message.text == "Помощь" or message.text == "помощь":
        bot.reply_to(message, "Выбери команду\n/id\n/name\n/start\n/photo\n/rmd\n")
    elif message.text == "1" or message.text == "5" or message.text == "6" or message.text == "7" or message.text == "8" or message.text == "0" :
        lv = 0
    elif message.text == "2":
        if lv == 0:
        	lv = 1
        else:
        	lv = 0
    elif message.text == "3":
        if lv == 2:
        	lv = 3
        else:
        	lv = 0
    elif message.text == "4":
        	if lv == 1:
        		lv = 2
        	else:
        		lv = 0
    elif message.text == "9":
        if lv == 3:
            lv = 0
            bot.reply_to(message, "you WIN", reply_markup=win())
    elif message.text == "you WIN":
         bot.reply_to(message, "Молодец", reply_markup=catalog_keyboard())
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
