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


class CartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'cart_screen'

        master_box = BoxLayout(orientation='vertical')
        size_bottom_panel_height = 0.08

        anchor = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=(1-size_bottom_panel_height))
        box = BoxLayout(orientation='vertical', size_hint_y=0.1)
        box.add_widget(Label(text='Корзина',
                             font_size=global_settings.FontSizes[3],
                             color=global_settings.Coffee_Colors[10]))
        box.add_widget(Label(text='пока пуста',
                             font_size=global_settings.FontSizes[2],
                             color=global_settings.Coffee_Colors[7]))

        anchor.add_widget(box)

        self.bottom_panel = BottomPanel('cart', size_hint_y=size_bottom_panel_height, spacing=5)
        self.bottom_panel.bind_callback_menu(self.callback_menu)
        self.bottom_panel.bind_callback_sales(self.callback_sales)
        self.bottom_panel.bind_callback_account(self.callback_account)

        master_box.add_widget(anchor)
        master_box.add_widget(self.bottom_panel)

        self.add_widget(master_box)

    def callback_menu(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = "menu_screen"

    def callback_sales(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = "sales_screen"

    def callback_account(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = "account_screen"
