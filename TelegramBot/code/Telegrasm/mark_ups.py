import telebot
import sqlite3
from telebot import types

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Меню', 'Сделать заказ')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Перейти к закускам', 'Отмена', 'Меню')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Выбрать способ получения', 'Отмена', 'Меню')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Забронировать столик', 'Возьму на месте', 'Отмена')

keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row('1', '2', '4', '6', 'Отмена')

keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row('Все верно', 'Добавить в заказ еще', 'Отмена')

keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard7.row('Оплата сейчас', 'Отмена')
