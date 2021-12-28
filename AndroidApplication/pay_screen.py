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


class PayScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'pay_screen'

        master_layout = BoxLayout(orientation='vertical')
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        box_in_center = BoxLayout(orientation='vertical',
                                  size_hint_x=0.7,
                                  size_hint_y=0.5)
        price = 0
        for prod in global_settings.Products_in_Cart:
            price += prod["price"] * prod["count"]
        self.price_label = Label(text="К оплате: {0}".format(price),
                                 font_size=global_settings.FontSizes[3],
                                 color=(0, 0, 0, 1))
        label_way_pay = Label(text="Выбирите способ оплаты:",
                              font_size=global_settings.FontSizes[2],
                              color=(0, 0, 0, 1))

        box_for_checkbox1 = BoxLayout(size_hint_x=0.5)
        box_for_checkbox1.add_widget(CheckBox(group="way_pay",
                                              active=True,
                                              color=(0, 0, 0, 1)))
        box_for_checkbox1.add_widget(Button(background_normal='images\\cash.png',
                                            size_hint_x=0.6))

        box_for_checkbox2 = BoxLayout(size_hint_x=0.5)
        box_for_checkbox2.add_widget(CheckBox(group="way_pay",
                                              active=False,
                                              color=(0, 0, 0, 1)))
        box_for_checkbox2.add_widget(Button(background_normal='images\\cards.png',
                                            size_hint_x=0.5))

        self.error_label = Label(text="Оплата пока доступна только при получении",
                                 color=(.9, .25, .15, 1))

        self.button_pay = Button(text='Оформить заказ',
                                 background_color=(.9, .25, .15, 1),
                                 background_normal='')
        self.button_pay.bind(on_press=self.callback_button_pay)

        box_in_center.add_widget(self.price_label)
        box_in_center.add_widget(label_way_pay)

        box_in_center.add_widget(box_for_checkbox1)
        box_in_center.add_widget(box_for_checkbox2)
        box_in_center.add_widget(self.error_label)

        box_in_center.add_widget(self.button_pay)

        anchor_layout.add_widget(box_in_center)
        master_layout.add_widget(anchor_layout)
        self.add_widget(master_layout)

    def callback_button_pay(self, instance):
        result = backend.SendOrder()
        if result:
            print("Номер заказа {0}".format(result))
        else:
            print("Произошла непредвиденная ошибка. Попробуйте позже.")
