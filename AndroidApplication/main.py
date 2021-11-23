import os

from kivy.app import App
from kivy.config import Config

import global_settings
import menu_screen
import registration_screen

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

import global_settings
import Backend.backend as backend


# Класс приложения
class CoffeeApp(App):
    def build(self):
        # Создаём менеджере экранов
        sm = ScreenManager()
        # Добавляем экраны
        sm.add_widget(login_screen.LoginScreen())
        sm.add_widget(registration_screen.RegistrationScreen())
        sm.add_widget(menu_screen.MenuScreen())
        sm.add_widget(sales_screen.SalesScreen())
        sm.add_widget(cart_screen.CartScreen())
        sm.add_widget(account_screen.AccountScreen())

        if os.path.exists('cookies'):
            sm.current = 'menu_screen'

        return sm


if __name__ == '__main__':
    # ==================================== #
    # Инициализируем глобальные переменные #
    # ==================================== #

    test_label_size = Label(text='get_size')
    font_scales = [1, 1.25, 1.5, 2, 2.5, 3, 4, 5]
    normal_font_size = test_label_size.font_size
    new_font_sizes = [normal_font_size * font_scale for font_scale in font_scales]
    global_settings.Init()
    global_settings.SetFontSizes(new_font_sizes)

    # ========================================== #
    # Установим цвет заднего фона для приложения #
    # Создадим окно приложения и запустим его.   #
    # ========================================== #

    Window.clearcolor = (248 / 255, 215 / 255, 191 / 255, 1)
    CoffeeApp().run()
