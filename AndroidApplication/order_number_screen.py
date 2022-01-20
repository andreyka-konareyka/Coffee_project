import os

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.factory import Factory


import global_settings
import Backend.backend as backend


class OrderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'order_number_screen'

        master_layout = BoxLayout(orientation='vertical')
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        box_in_center = BoxLayout(orientation='vertical',
                                  size_hint_x=0.7,
                                  size_hint_y=0.16)
        num = global_settings.OrderNumber
        self.label_order_number = Label(text="Номер заказа: {0}".format(num),
                                        font_size=global_settings.FontSizes[2],
                                        color=(0, 0, 0, 1))

        self.button_done = Button(text='Подтвердить получение',
                                  background_color=(.9, .25, .15, 1),
                                  background_normal='')
        self.button_done.bind(on_press=self.callback_button_done)
        global_settings.funcs_upd_order_number.append(self.update_order_number)

        box_in_center.add_widget(self.label_order_number)
        box_in_center.add_widget(self.button_done)

        anchor_layout.add_widget(box_in_center)
        master_layout.add_widget(anchor_layout)
        self.add_widget(master_layout)

    def update_order_number(self):
        num = global_settings.OrderNumber
        self.label_order_number.text = "Номер заказа: {0}".format(num)

    def callback_button_done(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = "menu_screen"
