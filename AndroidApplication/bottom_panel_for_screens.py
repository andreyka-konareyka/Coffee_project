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


import global_settings
import Backend.backend as backend


class BottomPanel(BoxLayout):
    def __init__(self, screen, **kwargs):
        super().__init__(**kwargs)

        self.button_menu = Button(text='Меню',
                                  font_size=global_settings.FontSizes[1],
                                  background_color=global_settings.Coffee_Colors[9 if screen == 'menu' else 6],
                                  background_normal='')

        self.button_sales = Button(text='Акции',
                                   font_size=global_settings.FontSizes[1],
                                   background_color=global_settings.Coffee_Colors[9 if screen == 'sales' else 6],
                                   background_normal='')

        self.button_cart = Button(text='Корзина',
                                  font_size=global_settings.FontSizes[1],
                                  background_color=global_settings.Coffee_Colors[9 if screen == 'cart' else 6],
                                  background_normal='')

        self.button_account = Button(text='Аккаунт',
                                     font_size=global_settings.FontSizes[1],
                                     background_color=global_settings.Coffee_Colors[9 if screen == 'account' else 6],
                                     background_normal='')

        self.add_widget(self.button_menu)
        self.add_widget(self.button_sales)
        self.add_widget(self.button_cart)
        self.add_widget(self.button_account)

    def bind_callback_menu(self, func):
        self.button_menu.bind(on_press=func)

    def bind_callback_sales(self, func):
        self.button_sales.bind(on_press=func)

    def bind_callback_cart(self, func):
        self.button_cart.bind(on_press=func)

    def bind_callback_account(self, func):
        self.button_account.bind(on_press=func)