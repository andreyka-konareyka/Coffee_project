from kivy.app import App
from kivy.config import Config

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

from global_settings import *
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

        try:
            cookies_file = open('cookies', 'r')
            sm.current = 'menu_screen'
        except Exception:
            pass

        return sm


if __name__ == '__main__':
    # Установим цвет заднего фона для приложения
    Window.clearcolor = (248 / 255, 215 / 255, 191 / 255, 1)
    # И запустим
    CoffeeApp().run()
