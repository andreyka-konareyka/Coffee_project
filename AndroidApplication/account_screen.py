import os

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
from bottom_panel_for_screens import BottomPanel


class AccountScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'account_screen'

        master_layout = BoxLayout(orientation='vertical')
        size_bottom_panel_height = 0.08

        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=(1-size_bottom_panel_height))
        self.button_sign_off = Button(text='Выйти',
                                      background_color=(.9, .25, .15, 1),
                                      background_normal='',
                                      size_hint=[0.5, 0.1])
        self.button_sign_off.bind(on_press=self.callback_button_sign_off)

        anchor_layout.add_widget(self.button_sign_off)

        self.bottom_panel = BottomPanel('account', size_hint_y=size_bottom_panel_height, spacing=5)
        self.bottom_panel.bind_callback_menu(self.callback_menu)
        self.bottom_panel.bind_callback_sales(self.callback_sales)
        self.bottom_panel.bind_callback_cart(self.callback_cart)

        master_layout.add_widget(anchor_layout)
        master_layout.add_widget(self.bottom_panel)

        self.add_widget(master_layout)

    def callback_menu(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = "menu_screen"

    def callback_sales(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = "sales_screen"

    def callback_cart(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = "cart_screen"

    def callback_button_sign_off(self, instance):
        os.remove('cookies')
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"
