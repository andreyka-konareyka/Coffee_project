import kivy
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

from kivy.graphics import Color, Rectangle, RoundedRectangle

import global_settings
import Backend.local_backend as lBackEnd
import Backend.backend as backend
from bottom_panel_for_screens import BottomPanel


class CountCartProductsWidget(BoxLayout):
    def __init__(self, id_in_cart_list, **kwargs):
        super().__init__(**kwargs)
        self.product = global_settings.Products_in_Cart[id_in_cart_list]
        if self.product is None:
            return
        self.item_id = self.product["id"]

        self.center_anchor = AnchorLayout(anchor_x='center',
                                          anchor_y='center')
        self.center_box_in_anchor = BoxLayout(orientation='vertical',
                                              size_hint=[0.6, 0.5])

        self.center_box_in_anchor.add_widget(Button(text=self.product["title"],
                               font_size=global_settings.FontSizes[1],
                               background_color=(1, 1, 0, 0/2),
                               size_hint_y=0.5))
        self.center_box_in_anchor.add_widget(Button(text="Цена: " + str(self.product["price"]),
                               font_size=global_settings.FontSizes[1],
                               background_color=(1, 1, 0, 0/2),
                               size_hint_y=0.5))
        #####################
        # Счётчик продуктов #
        #####################

        self.count_box = BoxLayout()

        button_delete_item = Button(background_normal='images/button_delete.png',
                                    size_hint_x=1)

        button_delete_item.bind(on_press=self.callback_button_delete_item)

        cart_product = global_settings.get_product_from_cart(self.item_id)
        count = 0 if cart_product is None else cart_product["count"]
        self.counter_cart_item = Button(text=str(count),
                                        size_hint_x=0.6,
                                        background_color=(1, 1, 1, 0))

        button_add_item = Button(background_normal='images/button_add.png',
                                 size_hint_x=1)
        button_add_item.bind(on_press=self.callback_button_add_item)

        self.count_box.add_widget(button_delete_item)
        self.count_box.add_widget(self.counter_cart_item)
        self.count_box.add_widget(button_add_item)

        global_settings.funcs_upd_cart.append(self.callback_edit_counter)

        ##################
        # Конец счётчика #
        ##################

        self.center_box_in_anchor.add_widget(self.count_box)

        self.center_anchor.add_widget(self.center_box_in_anchor)
        self.add_widget(self.center_anchor)

    def callback_button_delete_item(self, instance):
        lBackEnd.remove_from_cart_items_in_json(self.product)
        global_settings.update_cart_counters()

    def callback_button_add_item(self, instance):
        lBackEnd.add_cart_items_in_json(self.product)
        global_settings.update_cart_counters()

    def callback_edit_counter(self):
        cart_product = global_settings.get_product_from_cart(self.item_id)
        count = 0 if cart_product is None else cart_product["count"]
        self.counter_cart_item.text = str(count)


class CartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'cart_screen'

        window_width = kivy.core.window.Window.width

        self.master_box = BoxLayout(orientation='vertical')
        size_bottom_panel_height = 0.08

        self.scroll_panel = ScrollView()
        self.scroll_panel.do_scroll_x = False
        self.scroll_panel.do_scroll_y = True

        self.cart_items = BoxLayout(orientation='vertical', spacing=5)
        self.cart_items.size_hint_y = None
        data_cart = global_settings.Products_in_Cart
        count_items = len(data_cart)
        self.cart_items.height = int(window_width * count_items / 2)

        # ============================= #
        # Заполняем клеточки продуктами #
        # ============================= #

        size_x = window_width - 5
        size_y = window_width / 2 - 5
        for i in range(count_items):
            item = BoxLayout()
            pos_x = 2
            pos_y = (window_width / 2 + 1.5) * (count_items - i - 1)

            with item.canvas:
                Color(*global_settings.Global_Theme_Colors[5][:-1])
                # Rectangle(pos=[pos_x, pos_y], size=[size_x, size_y])
                RoundedRectangle(pos=[pos_x, pos_y], size=[size_x, size_y], radius=[25, 25, 25, 25])

            item.add_widget(Button(background_color=(1, 1, 1, 2/2),
                                   background_normal='images/' + data_cart[i]["image"],
                                   size_hint_x=0.5))
            """item.add_widget(Button(text="Кол-во = {0}".format(data_cart[i]["count"]),
                                   font_size=global_settings.FontSizes[1],
                                   background_color=(1, 1, 0, 1/2),
                                   size_hint_x=0.5))"""
            item.add_widget(CountCartProductsWidget(i, size_hint_x=0.5, orientation='vertical'))

            self.cart_items.add_widget(item)

        self.scroll_panel.add_widget(self.cart_items)

        self.pay_button = Button(text="Оформить заказ",
                                 font_size=global_settings.FontSizes[1],
                                 size_hint_y=size_bottom_panel_height,
                                 background_color=(.9, .25, .15, 1),
                                 background_normal='')
        self.pay_button.bind(on_press=self.callback_pay)

        self.bottom_panel = BottomPanel('cart', size_hint_y=size_bottom_panel_height, spacing=5)
        self.bottom_panel.bind_callback_menu(self.callback_menu)
        self.bottom_panel.bind_callback_sales(self.callback_sales)
        self.bottom_panel.bind_callback_account(self.callback_account)

        self.master_box.add_widget(self.scroll_panel)
        self.master_box.add_widget(self.pay_button)
        self.master_box.add_widget(self.bottom_panel)

        self.add_widget(self.master_box)

    def callback_pay(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = "pay_screen"

    def callback_menu(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = "menu_screen"

    def callback_sales(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = "sales_screen"

    def callback_account(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = "account_screen"

    def callback_clear_widgets(self, instance):
        self.box.clear_widgets()
