#########################################################
#######   Включение DebugMode для отладки API    ########
#########################################################

import global_settings

# True  -  для работы на компьютере
# False -  для андроида

debugMode = True #     <--------------------------------- изменять здесь

#########################################################
#######                                          ########
#########################################################


import os

import kivy.uix.screenmanager
from kivy.app import App
from kivy.config import Config

Config.set("graphics", "width", 640)    # Установка разрешения, похожего не телефон
Config.set("graphics", "height", 960)   # Нужно для отладки на ПК

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.factory import Factory
from kivy.core.window import Window

import login_screen
import registration_screen
import menu_screen
import account_screen
import sales_screen
import cart_screen
import pay_screen
import order_number_screen

import Backend.backend as backend
import Backend.local_backend as lBackEnd


# Класс приложения
class CoffeeApp(App):
    def build(self):
        # Создаём менеджере экранов
        self.sm = ScreenManager()
        # Добавляем экраны
        self.sm.add_widget(login_screen.LoginScreen())
        self.sm.add_widget(registration_screen.RegistrationScreen())
        self.sm.add_widget(menu_screen.MenuScreen())
        self.sm.add_widget(sales_screen.SalesScreen())
        self.sm.add_widget(pay_screen.PayScreen())
        self.sm.add_widget(order_number_screen.OrderScreen())
        self.sm.add_widget(account_screen.AccountScreen())

        self.cart_Screen = cart_screen.CartScreen()
        self.sm.add_widget(self.cart_Screen)

        global_settings.funcs_upd_cart.append(self.update_cart_Screen)


        if os.path.exists('cookies'):
            self.sm.current = 'menu_screen'
            cookies_file = open('cookies', 'r')
            str_number = cookies_file.readline()
            global_settings.SetCurrentUser(str_number)

        return self.sm

    def update_cart_Screen(self):
        flag_in_cart = True if self.sm.current == 'cart_screen' else False

        self.sm.remove_widget(self.cart_Screen)
        self.cart_Screen = cart_screen.CartScreen()
        self.sm.add_widget(self.cart_Screen)

        if flag_in_cart:
            self.sm.transition = kivy.uix.screenmanager.NoTransition()
            self.sm.current = 'cart_screen'
            self.sm.transition = kivy.uix.screenmanager.SlideTransition()


if __name__ == '__main__':
    # ==================================== #
    # Инициализируем глобальные переменные #
    # ==================================== #

    test_label_size = Label(text='get_size')
    font_scales = [1, 1.25, 1.5, 2, 2.5, 3, 4, 5]
    normal_font_size = test_label_size.font_size
    new_font_sizes = [normal_font_size * font_scale for font_scale in font_scales]
    global_settings.Init()
    global_settings.SetDebugMode(debugMode)
    global_settings.SetFontSizes(new_font_sizes)
    global_settings.Products_in_Cart = lBackEnd.get_cart_items_from_json()

    # ========================================== #
    # Установим цвет заднего фона для приложения #
    # Создадим окно приложения и запустим его.   #
    # ========================================== #

    # Window.clearcolor = (248 / 255, 215 / 255, 191 / 255, 1)
    Window.clearcolor = (1, 1, 1, 1)
    CoffeeApp().run()
