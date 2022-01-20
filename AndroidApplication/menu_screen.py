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
# from kivy.core.window import Window

from kivy.graphics import Color, Rectangle, RoundedRectangle

import global_settings
import Backend.backend as backend
import Backend.local_backend as lBackEnd
from bottom_panel_for_screens import BottomPanel


class PriceBoxWidget(BoxLayout):
    def __init__(self, id_in_menu_list, **kwargs):
        super().__init__(**kwargs)
        self.product = global_settings.MenuProducts[id_in_menu_list]
        if self.product is None:
            return
        self.item_id = self.product["id"]

        self.add_widget(Button(text="Цена: " + str(self.product["price"]),
                               font_size=global_settings.FontSizes[1],
                               background_color=(1, 1, 1, 0),
                               size_hint_x=0.5))

        button_delete_item = Button(background_normal='images/button_delete.png',
                                    size_hint_x=0.25)

        button_delete_item.bind(on_press=self.callback_button_delete_item)

        cart_product = global_settings.get_product_from_cart(self.item_id)
        count = 0 if cart_product is None else cart_product["count"]
        self.counter_cart_item = Button(text=str(count),
                                        size_hint_x=0.15,
                                        background_color=(1, 1, 1, 0))

        button_add_item = Button(background_normal='images/button_add.png',
                                 size_hint_x=0.25)
        button_add_item.bind(on_press=self.callback_button_add_item)

        global_settings.funcs_upd_cart.append(self.callback_edit_counter)

        self.add_widget(button_delete_item)
        self.add_widget(self.counter_cart_item)
        self.add_widget(button_add_item)

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


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'menu_screen'

        window_width = kivy.core.window.Window.width

        self.layout = BoxLayout(orientation='vertical', spacing=5)
        size_bottom_panel_height = 0.08

        # ========================== #
        # Основное пространство меню #
        # ========================== #

        self.scroll_panel_shell = BoxLayout(size_hint=[1, 1 - size_bottom_panel_height])
        self.scroll_panel = ScrollView()
        self.scroll_panel.do_scroll_x = False
        self.scroll_panel.do_scroll_y = True
        my_grid = GridLayout(cols=2, spacing=5)
        my_grid.size_hint_y = None

        menu_products = backend.GetListProducts()
        global_settings.MenuProducts = menu_products
        count_menu = len(menu_products)
        my_grid.height = int(window_width * ((count_menu + 1) // 2) * 2 / 3)

        # ============================= #
        # Заполняем клеточки продуктами #
        # ============================= #

        self.price_boxes = []

        size_x = window_width / 2 - 5
        size_y = window_width * 2 / 3 - 5
        for i in range(count_menu):
            bl = BoxLayout(orientation='vertical')
            pos_x = (window_width + 5) / 2 * (i % 2) + 2
            pos_y = (window_width * 2 / 3 + 1/5) * ((count_menu + 1)//2 - (i // 2) - 1)

            with bl.canvas:
                Color(*global_settings.Global_Theme_Colors[5][:-1])
                # Rectangle(pos=[pos_x, pos_y], size=[size_x, size_y])
                RoundedRectangle(pos=[pos_x, pos_y], size=[size_x, size_y], radius=[25, 25, 25, 25])

            bl.add_widget(Button(background_color=(1, 1, 1, 1),
                                 background_normal='images/' + menu_products[i]["image"],
                                 size_hint_y=0.7))

            description_box = BoxLayout(orientation='vertical', size_hint_y=0.3)
            description_box.add_widget(Button(text=menu_products[i]["title"],
                                              font_size=global_settings.FontSizes[1],
                                              background_color=(1, 1, 1, 0),
                                              size_hint_y=0.4))
            # price_box = BoxLayout(size_hint_y=0.6)
            self.price_boxes.append(PriceBoxWidget(i, size_hint_y=0.6))

            description_box.add_widget(self.price_boxes[-1])
            bl.add_widget(description_box)
            # bl.add_widget(Button(text=str(i)))

            my_grid.add_widget(bl)
            # background_color=(203/255, 170/255, 132/255, 1),

        self.scroll_panel.add_widget(my_grid)

        # =============================================== #
        # Добавляем нижнюю панель навигации по приложению #
        # =============================================== #

        self.bottom_panel = BottomPanel('menu', size_hint=[1, size_bottom_panel_height],
                                        spacing=5)

        self.bottom_panel.bind_callback_sales(self.callback_button_sales)
        self.bottom_panel.bind_callback_cart(self.callback_button_cart)
        self.bottom_panel.bind_callback_account(self.callback_button_account)

        self.scroll_panel_shell.add_widget(self.scroll_panel)
        self.layout.add_widget(self.scroll_panel_shell)
        self.layout.add_widget(self.bottom_panel)

        self.add_widget(self.layout)

    def callback_button_sales(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = "sales_screen"

    def callback_button_cart(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = "cart_screen"

    def callback_button_account(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = "account_screen"