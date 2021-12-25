import telebot
import sqlite3
from telebot import types
import mark_ups as nv
from pyqiwip2p import QiwiP2P
import random

bot = telebot.TeleBot("2076232517:AAEWXXnJJk7f6UOmZDKU1qztvVqA3poB0us")

connection = sqlite3.connect('C:/Users/andry/source/repos/Coffee_project/TelegramBot/code/testy.db', check_same_thread=False)
cursor = connection.cursor() 
p2p = QiwiP2P(auth_key=
              "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjBhcDk4My0wMCIsInVzZXJfaWQiOiI3OTY4OTI4NTE1NSIsInNlY3JldCI6ImYzYTc3YjdjN2M1N2FjNzExZGE3NTFkYWMzZWQyMTlmMmViOTZlMGU3NzRkMGJmOThiZjhkMjE1OGIwZTRhM2UifX0=")

state = 0
#Синхронизация удаления кол-ва элементов из БД(временное) конечное удаление после оплаты
def update_bread_list():
    lst = []
    with connection:
        cursor.execute("SELECT * FROM `sklad` WHERE `category` = ?", ("bread",))
        records = cursor.fetchall()
        for row in records:
            if row[4] > 0:
                lst.append(row[2])
    return lst

def update_water_list():
    lst = []
    with connection:
        cursor.execute("SELECT * FROM `sklad` WHERE `category` = ?", ("water",))
        records = cursor.fetchall()
        for row in records:
            if row[4] > 0:
                lst.append(row[2])
    return lst

def update_price_list():
    price_list = {}
    with connection:
        cursor.execute("SELECT * FROM `sklad` WHERE `category` = ?", ("bread",))
        records = cursor.fetchall()
        temp_ = {}
        for row in records:
            temp_[row[2]] = row[5]
        price_list["category_bread"] = temp_

        cursor.execute("SELECT * FROM `sklad` WHERE `category` = ?", ("water",))
        records = cursor.fetchall()
        temp_ = {}
        for row in records:
            temp_[row[2]] = row[5]
        price_list["category_water"] = temp_
    return price_list

napitki = update_water_list()
zakuski = update_bread_list()
price_list = update_price_list()

zakaz = {"user_id": None, "number_req": None,
        "category_bread": None, "category_water": None, 
        "price":0, "book_a_table": [False, None], "on_way": False, "was_priced": False}


@bot.message_handler(commands=['start'])
def start_message(message):

    
    bot.send_message(message.chat.id, """Я - бот, созданный помочь вам сделать свой заказ в кофейне. 
    на панели кнопок вы можете взаимодействовать со мной прямо как младенец с матерью.""",
    reply_markup= nv.keyboard1)
    bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTSlhk9afeayllwuZ5fYksEzlMOyUvQAChwQAAsFQ8Fdw4ImIvUIyYSIE')

    user = bot.get_me()
    zakaz["user_id"] = user.id
    if not user_exists(user.id):
        add_user(user.id)
    if (state == 0):
        return

@bot.message_handler(content_types=['text'])
def send_text(message):
   global state, zakaz
   user = bot.get_me()
   zakaz["user_id"] = user.id
   if (state == 0):

       if message.text.lower() == 'сделать заказ':
           bot.send_message(message.chat.id, "Давайте посмотрим на напитки", reply_markup=nv.keyboard2)
           c = menu_napitki()
           bot.send_message(message.chat.id, c)

           di = {}
           zakaz["category_water"] = di
           for i in range(len(napitki)):
                zakaz["category_water"][napitki[i]] = 0
           di = {}
           zakaz["category_bread"] = di
           for i in range(len(zakuski)):
                zakaz["category_bread"][zakuski[i]] = 0 
           

           state = 3
           return
       elif message.text.lower() == 'меню':
           c = menu()
           bot.send_message(message.chat.id, c)
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup=nv.keyboard1)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')

   elif (state == 3):

       if message.text in napitki:
           
           zakaz["category_water"][message.text] += 1
           bot.send_message(message.chat.id, "Хорошо, добавляю в заказ" + " " + "+1" + message.text + "." + " " + list_zakaza())
           update_price()
           bot.delete_message(message.chat.id, message.message_id)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDixxhw7Ee4Di1jlt8xnWm0WjGEgS3_gAC4gMAAtrs-Fd0htpDYisamyME')
           return

       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup= nv.keyboard1)
           zakaz_set_default()
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return

       elif message.text.lower() == "меню":
           c = menu_napitki()
           bot.send_message(message.chat.id, c, nv.keyboard2)
           

       elif message.text.lower() == "перейти к закускам":
           state = 4
           bot.send_message(message.chat.id, "Давайте посмотрим на закуски", reply_markup= nv.keyboard3)
           c = menu_zakuski()
           bot.send_message(message.chat.id, c)
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup= nv.keyboard2)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')


   elif (state == 4):
       
       if message.text in zakuski:
           zakaz["category_bread"][message.text] += 1
           bot.send_message(message.chat.id, "Хорошо, добавляю в заказ" + " " + "+1" + message.text + "." + " " + list_zakaza())
           update_price()
           bot.delete_message(message.chat.id, message.message_id)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDixxhw7Ee4Di1jlt8xnWm0WjGEgS3_gAC4gMAAtrs-Fd0htpDYisamyME')
           return

       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup= nv.keyboard1)
           zakaz_set_default()
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return

       elif message.text.lower() == "меню":
           c = menu_zakuski() 
           bot.send_message(message.chat.id, c, nv.keyboard3)

       elif message.text.lower() == "выбрать способ получения":
           state = 5
           bot.send_message(message.chat.id, "Давайте выберем способ получения", reply_markup= nv.keyboard4)
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup= nv.keyboard3)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')

   elif (state == 5):
       if  message.text.lower() == "забронировать столик":
           state = 6
           zakaz["book_a_table"] = [True, None]
           bot.send_message(message.chat.id, "Хорошо, давайте укажем на сколько человек вы хотите забронировать столик", reply_markup= nv.keyboard5)
           return
       
       if  message.text.lower() == "возьму на месте":
           state = 7
           zakaz["book_a_table"] = [False, None]
           zakaz["on_way"] = True
           bot.send_message(message.chat.id, "Хорошо, предоставляю вам ваш лист заказа", reply_markup= nv.keyboard6) 
           c = list_zakaza()
           bot.send_message(message.chat.id, c, reply_markup= nv.keyboard6)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDixphw7DK_RaTEraL542wlmZuj3X1zwACEAQAAno18VfmYZ9rnxDpLyME')

           return

       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup=nv.keyboard1)
           zakaz_set_default()
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup=nv.keyboard4)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')

   elif (state == 6):
       if message.text.lower() in ["1", "2", "4", "6"]:
            zakaz["book_a_table"][1] = message.text
            state = 7
            bot.send_message(message.chat.id, "Хорошо, предоставляю вам ваш лист заказа", reply_markup=nv.keyboard6)
            c = list_zakaza()
            bot.send_message(message.chat.id, c + " " + "Также вы пожелали отдохнуть компанией из" + " " + zakaz["book_a_table"][1], reply_markup=nv.keyboard6)
            bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDixphw7DK_RaTEraL542wlmZuj3X1zwACEAQAAno18VfmYZ9rnxDpLyME')
            
            return

       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup=nv.keyboard1)
           zakaz_set_default()
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return

       else:
           bot.send_message(message.chat.id, "Я вас не понимаю, пользуйтесь кнопками, которые сделал мой создатель.", reply_markup=nv.keyboard4)
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDTnFhlOh4NmitMn0KQ-rWTbQMDDDs_gACxwQAArwc8VcCfsqE62W_3yIE')

   elif (state == 7):

       if message.text.lower() == 'все верно':
           state = 8
           bot.send_message(message.chat.id, "Хорошо, давайте перейдем к оплате", reply_markup=nv.keyboard7)
           return

       elif message.text.lower() == 'добавить в заказ еще':
           state = 3
           bot.send_message(message.chat.id, "Хорошо, давайте выберем напиток", reply_markup=nv.keyboard2)
           return

   elif (state == 8):
       if zakaz["price"] < 25:
           state = 0
           bot.send_message(message.chat.id, "Отменяю заказ, так как вы заказали меньше допустимой цены. Чего желаете?", reply_markup=nv.keyboard1)
           zakaz_set_default()
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return
       if message.text.lower() == "оплата сейчас":
           print(zakaz["user_id"])
           comment = str(zakaz["user_id"]) + "_" + str(random.randint(1000, 9999))
           zakaz["number_req"] = comment
           bill = p2p.bill(amount= price, lifetime = 15, comment = comment)
           bot.send_message(message.chat.id, F"Ваш счет на оплату готов:\n{bill.pay_url}\nКомментарий к заказу: {comment}" )
           user = bot.get_me()
           add_check(user.id, bill.bill_id)
           waiting_for_paid(bill.bill_id, user.id)
           return
       elif message.text.lower() == "отмена":
           state = 0
           bot.send_message(message.chat.id, "Хорошо, отменяю ваш заказ. Чего желаете?", reply_markup=nv.keyboard1)
           zakaz_set_default()
           bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDToVhlPtOPbCHx_0q4iblLkO1qEPJRAACIAQAArXP8FcX_VjrZf6uNSIE')
           return
       
   elif (state == 9):
       bot.send_message(message.chat.id, "Хорошо, воспользуйтесь кодом комментария для получения заказа. Что-то еще?", reply_markup=nv.keyboard1)
       bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAEDjThhxLf5rF7sahZc7BUqUt4jMAOd-QACigMAAlZy8Fe-tgkYYJYTJCME')
       state = 0

def waiting_for_paid(bill_id, user_id):
    global state, zakaz
    info = get_check(bill_id)
    if info != False:
        if str(p2p.check(bill_id = bill_id).status) == "PAID":
            state = 9
            zakaz["was_priced"] = True
            delete_check(bill_id)
            pool_request(bill_id, user_id)
    else:
        bot.send_message(message.chat.id, "Счет не найден")
        state = 8


def pool_request(bill_id, user_id):
    global zakaz
   
    res = "Заказано:"
    s = ""
    for i in range(len(zakaz["category_bread"])):
        if (zakaz["category_bread"][zakuski[i]] != 0):
            s += str(zakaz["category_bread"][zakuski[i]]) + " " + zakuski[i] + " "
           
    res += s
    s = ""
    for i in range(len(zakaz["category_water"])):
        if (zakaz["category_water"][napitki[i]]) != 0:
            s += str(zakaz["category_water"][napitki[i]]) + " " + napitki[i] + " "
            
    res += s

    book = 0
    if (zakaz["book_a_table"][0] == False):
        book = 0
    else:
        book = zakaz["book_a_table"][1]


    with connection:
        cursor.execute("INSERT INTO `request` (`user_id`, `num`, `req`, `book`) VALUES (?, ?, ?, ?)", (user_id, bill_id, res, book,))
       
    


def list_zakaza():
    global price, zakaz
    res = "Вы заказали:"
    s = ""
    price = 0
    for i in range(len(zakaz["category_bread"])):
        if (zakaz["category_bread"][zakuski[i]] != 0):
            s += str(zakaz["category_bread"][zakuski[i]]) + " " + zakuski[i] + " "
            price += zakaz["category_bread"][zakuski[i]]*price_list["category_bread"][zakuski[i]]
    res += s
    s = ""
    for i in range(len(zakaz["category_water"])):
        if (zakaz["category_water"][napitki[i]]) != 0:
            s += str(zakaz["category_water"][napitki[i]]) + " " + napitki[i] + " "
            price += zakaz["category_water"][napitki[i]]*price_list["category_water"][napitki[i]]
    res += s
  
    return  res + " " + "На общую сумму " + " " + str(price)



def zakaz_set_default():
    global zakaz
    zakaz = {"user_id": None, "number_req": None,
        "category_bread": None, "category_water": None, 
        "price":0, "book_a_table": False, "on_way": False, "was_priced": False}


def menu():
    c = "У нас имеются напитки:"
    for i in range(len(napitki)):
        c += " "
        c += napitki[i]
    b = "У нас имеются закуски:"            
    for j in range(len(zakuski)):
        b += " "
        b += zakuski[j]
    res = c + "\n" + b
    return res

def menu_napitki():
    c = "У нас имеются напитки:"
    for i in range(len(napitki)):
        c += " "
        c += napitki[i]
    return c

def menu_zakuski():
    c = "У нас имеются закуски:"
    for i in range(len(zakuski)):
        c += " "
        c += zakuski[i]
    return c

def is_number(st):
    try:
        int(st)
        return True
    except ValueError:
        return False

def update_price():
    global price, zakaz
    price = 0
 
    for i in range(len(zakaz["category_bread"])):
        if (zakaz["category_bread"][zakuski[i]] != 0):

            price += zakaz["category_bread"][zakuski[i]]*price_list["category_bread"][zakuski[i]]
    
    for i in range(len(zakaz["category_water"])):
        if (zakaz["category_water"][napitki[i]]) != 0:
            price += zakaz["category_water"][napitki[i]]*price_list["category_water"][napitki[i]]

    zakaz["price"] = price

def user_exists(user_id):
    with connection:
        result = cursor.execute("SELECT * FROM `clients` WHERE `user_id` = ?", (user_id,)).fetchall()
        return bool(len(result))

def add_user(user_id):
    with connection:
        return cursor.execute("INSERT INTO `clients` (`user_id`) VALUES (?)", (user_id,))

def add_check(user_id, bill_id):
    with connection:
        cursor.execute("INSERT INTO `check` (`user_id`, `bill_id`) VALUES (?, ?)", (user_id, bill_id,))

def get_check(bill_id):
    with connection:
        result = cursor.execute("SELECT * FROM `check` WHERE `bill_id` = ?", (bill_id,)).fetchmany(1)
        if not bool(len(result)):
            return False
        else:
            return result[0]

def delete_check(bill_id):
    with connection:
        return cursor.execute("DELETE FROM `check` WHERE `bill_id` = ?", (bill_id,))

bot.infinity_polling()



