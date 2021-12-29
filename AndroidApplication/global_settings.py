import Backend.local_backend as lBackEnd


def Init():
    global DebugMod, FontSizes, Coffee_Colors, CurrentUser, Second_Theme_Colors, Global_Theme_Colors, MenuProducts, Products_in_Cart, OrderNumber
    global funcs_upd_cart, funcs_upd_order_number

    funcs_upd_cart = []
    funcs_upd_order_number = []

    DebugMod = True

    CurrentUser = "+78005553535"

    # Для Пк        25-32
    # Для Android   50
    FontSizes = [25]

    Coffee_Colors = [(81 / 255, 56 / 255, 42 / 255, 1),

                     (237 / 255, 214 / 255, 171 / 255, 1),
                     (224 / 255, 191 / 255, 156 / 255, 1),
                     (203 / 255, 170 / 255, 132 / 255, 1),
                     (198 / 255, 162 / 255, 119 / 255, 1),

                     (201 / 255, 149 / 255, 100 / 255, 1),
                     (183 / 255, 136 / 255, 97 / 255, 1),
                     (177 / 255, 129 / 255, 89 / 255, 1),
                     (166 / 255, 117 / 255, 82 / 255, 1),

                     (156 / 255, 108 / 255, 65 / 255, 1),
                     (139 / 255, 93 / 255, 61 / 255, 1),
                     (132 / 255, 83 / 255, 58 / 255, 1),
                     (121 / 255, 76 / 255, 53 / 255, 1),

                     (103 / 255, 68 / 255, 47 / 255, 1),
                     (95 / 255, 66 / 255, 44 / 255, 1),
                     (82 / 255, 55 / 255, 39 / 255, 1),
                     (61 / 255, 43 / 255, 37 / 255, 1)]

    Second_Theme_Colors = [(81 / 255, 56 / 255, 42 / 255, 1),

                           (0, 0, 0, 1),
                           (0, 0, 0, 1),
                           (0, 0, 0, 1),
                           (0, 0, 0, 1),

                           (0, 0, 0, 1),
                           (0, 0, 0, 1),
                           (0, 0, 0, 1),
                           (0, 0, 0, 1),

                           (1, 1, 1, 1),
                           (1, 1, 1, 1),
                           (1, 1, 1, 1),
                           (1, 1, 1, 1),

                           (1, 1, 1, 1),
                           (1, 1, 1, 1),
                           (1, 1, 1, 1),
                           (1, 1, 1, 1)]

    Global_Theme_Colors = Coffee_Colors
    MenuProducts = []
    Products_in_Cart = []
    OrderNumber = ''


def SetDebugMode(new_mode):
    global DebugMod
    DebugMod = new_mode


def SetFontSizes(array_sizes):
    global FontSizes
    FontSizes = array_sizes


def SetColors(new_colors):
    global Coffee_Colors
    Coffee_Colors = new_colors


def SetCurrentUser(user_number):
    global CurrentUser
    CurrentUser = user_number


def get_product_from_cart(id):
    for p in Products_in_Cart:
        if p["id"] == id:
            return p
    return None


def get_product_from_menu(id):
    for p in MenuProducts:
        if p["id"] == id:
            return p
    return None


def update_cart_counters():
    global Products_in_Cart
    Products_in_Cart = lBackEnd.get_cart_items_from_json()
    for func in funcs_upd_cart:
        func()


def update_order_number():
    for func in funcs_upd_order_number:
        func()


def set_order_number(new_number):
    global OrderNumber
    OrderNumber = new_number
