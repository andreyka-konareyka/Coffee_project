import telebot
from telebot import types

bot = telebot.TeleBot("2076232517:AAEWXXnJJk7f6UOmZDKU1qztvVqA3poB0us")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Меню', 'Сделать заказ')

'''Потом надо убрать и из БД уже предоставлять товар'''
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Перейти к закускам','Латте', 'Капучинно', 'Отмена', 'Меню')

'''Потом надо убрать и из БД уже предоставлять товар'''
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Выбрать способ получения', 'Булочка', 'Круасан', 'Отмена', 'Меню')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Забронировать столик', 'Возьму на месте', 'Отмена')

keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row('1', '2', '4', '6', 'Отмена')

keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row('Все верно', 'Добавить в заказ еще', 'Отмена')

keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard7.row('Оплата сейчас', 'Оплата на месте', 'Отмена')

state = 0

'''Потом надо убрать и из БД уже предоставлять товар'''
napitki = ['Латте', 'Капучинно']
zakuski = ['Булочка', 'Круасан']

'''Потом надо убрать. БД тут'''
zakaz = {}


@bot.message_handler(commands=['start'])
def start_message(message):
   
    bot.send_message(message.chat.id, """Я - бот, созданный помочь вам сделать свой заказ в кофейне. 
    на панели кнопок вы можете взаимодействовать со мной прямо как младенец с матерью.""",
    reply_markup=keyboard1)

    bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTSlhk9afeayllwuZ5fYksEzlMOyUvQAChwQAAsFQ8Fdw4ImIvUIyYSIE')
    if (state == 0):
        return



@bot.message_handler(content_types=['text'])
def send_text(message):
   global state

   if (state == 0):

       if message.text.lower() == 'сделать заказ':
           bot.send_message(message.chat.id, "Давайте посмотрим на напитки", reply_markup=keyboard2)
           state = 3
           print(0 , "Сделаем заказ")
           return
       elif message.text.lower() == 'меню':
           '''BD'''
           print(0, "Покажем меню")
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup=keyboard1)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')

   elif (state == 3):

       if message.text in napitki:
           bot.send_message(message.chat.id, "Хорошо, заказываем" + " " + message.text + " " + "." + "Но сколько? Введите конкретное значение")
           print(3, "Формирование заказа. Напитки")

           '''Надо учитывать заказ более одного напитка в кол-ве'''
           return

       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup=keyboard1)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return

       elif message.text.lower() == "меню":
           '''обращение к БД за напитками'''
           print(3, "Покажем меню")
           bot.send_message(message.chat.id, "*Вот меню напитков*", keyboard2)

       elif message.text.lower() == "перейти к закускам":
           state = 4
           print(3, "Переход с напитков на закуски")
           bot.send_message(message.chat.id, "Давайте посмотрим на закуски", reply_markup=keyboard3)
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup=keyboard2)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')


   elif (state == 4):

       if message.text in zakuski:
           bot.send_message(message.chat.id, "Хорошо, заказываем" + " " + message.text + " " + "." + "Но сколько? Введите конкретное значение")
           print(4, "Формирование заказа. Закуски")

           '''Надо учитывать заказ более одного напитка в кол-ве'''
           return

       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup=keyboard1)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return

       elif message.text.lower() == "меню":
           '''обращение к БД за напитками'''
           print(3, "Покажем меню")
           bot.send_message(message.chat.id, "*Вот меню закусок*" + zakuski, keyboard3)

       elif message.text.lower() == "выбрать способ получения":
           state = 5
           print(4, "Переход к способу получения")
           bot.send_message(message.chat.id, "Давайте выберем способ получения", reply_markup=keyboard4)
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup=keyboard3)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')

   elif (state == 5):
       if  message.text.lower() == "забронировать столик":
           state = 6
           bot.send_message(message.chat.id, "Хорошо, давайте укажем на сколько человек вы хотите забронировать столик", reply_markup=keyboard5)
           return
       
       if  message.text.lower() == "возьму на месте":
           state = 7
           bot.send_message(message.chat.id, "Хорошо, предоставляю вам ваш лист заказа", reply_markup=keyboard6) 
           '''Нужно как-то список всего из заказа предоставить'''
           return

       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup=keyboard1)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup=keyboard4)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')

   elif (state == 6):
       if message.text.lower() in ["1", "2", "4", "6"]:
            '''Куда-то отправляем кол-во людей за столиком (message.text)'''
            state = 7
            bot.send_message(message.chat.id, "Хорошо, предоставляю вам ваш лист заказа", reply_markup=keyboard6)
            '''Нужно как-то список всего из заказа предоставить'''
            return

       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup=keyboard1)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup=keyboard4)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')

   elif (state == 7):

       if message.text.lower() == 'все верно':
           state = 8
           bot.send_message(message.chat.id, "Хорошо, давайте выберем способ оплаты", reply_markup=keyboard7)
           return

       elif message.text.lower() == 'добавить в заказ еще':
           state = 9
           bot.send_message(message.chat.id, "Хорошо, давайте выберем напиток", reply_markup=keyboard2)
           return

       
       
   elif (state == 9):

       if message.text in napitki:
           bot.send_message(message.chat.id, "Хорошо, заказываем" + " " + message.text + " " + "." + "Но сколько? Введите конкретное значение")
           print(3, "Формирование заказа. Напитки")

           '''Надо учитывать заказ более одного напитка в кол-ве'''
           return

       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup=keyboard1)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return

       elif message.text.lower() == "меню":
           '''обращение к БД за напитками'''
           print(3, "Покажем меню")
           bot.send_message(message.chat.id, "*Вот меню напитков*" + napitki, keyboard2)

       elif message.text.lower() == "перейти к закускам":
           state = 10
           print(3, "Переход с напитков на закуски")
           bot.send_message(message.chat.id, "Давайте посмотрим на закуски", reply_markup=keyboard3)
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup=keyboard2)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')

   elif (state == 10):

       if message.text in zakuski:
           bot.send_message(message.chat.id, "Хорошо, заказываем" + " " + message.text + " " + "." + "Но сколько? Введите конкретное значение")
           print(4, "Формирование заказа. Закуски")

           '''Надо учитывать заказ более одного напитка в кол-ве'''
           return

       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup=keyboard1)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return

       elif message.text.lower() == "меню":
           '''обращение к БД за напитками'''
           print(3, "Покажем меню")
           bot.send_message(message.chat.id, "*Вот меню закусок*" + zakuski, keyboard3)

       elif message.text.lower() == "выбрать способ получения":
           state = 8
           print(4, "Переход к способу получения")
           bot.send_message(message.chat.id, "Давайте выберем способ получения", reply_markup=keyboard4)
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup=keyboard3)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')

   elif (state == 8):
       '''Здесь обработка оплаты сейчас/на месте'''
       pass









   

  

bot.infinity_polling()


