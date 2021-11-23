def Init():
    global DebugMod, FontSizes, Coffee_Colors, CurrentUser

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
