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

import global_settings
import Backend.backend as backend


# Виджет входа
class LoginWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        form_sign_in = BoxLayout(orientation="vertical",
                                 size_hint=(.8, .4),
                                 spacing=3)

        self.label_sign_in = Label(text="Вход",
                                   color=global_settings.Coffee_Colors[0],
                                   font_size=global_settings.FontSizes[3],
                                   size_hint=(1, 0.7))

        label_enter_number = Label(text="Номер:",
                                   color=global_settings.Coffee_Colors[0],
                                   size_hint=(1, 0.3))
        ''' Ввод номера телефона '''
        self.login_input = TextInput(multiline=False,
                                     size_hint=(1, 0.7))

        label_enter_password = Label(text="Пароль:",
                                     color=global_settings.Coffee_Colors[0],
                                     size_hint=(1, 0.3))
        ''' Ввод пароля '''
        self.password_input = TextInput(multiline=False,
                                        size_hint=(1, 0.7))

        box_buttons = BoxLayout(size_hint=(1, 0.7))

        self.button_sign_in = Button(text="Войти",
                                     size_hint=(.65, 1),
                                     font_size=global_settings.FontSizes[1])

        self.button_registration = Button(text="Регистрация",
                                          size_hint=(.35, 1),
                                          font_size=global_settings.FontSizes[1])

        '''
            Текст об ошибке при входе.
            Изначально пустой текст.
        '''
        self.label_password_invalid = Label(text="",
                                            color=(1, 0, 0, 1),
                                            font_size=global_settings.FontSizes[1],
                                            size_hint=(1, 0.7))

        """ Добавляем виджеты в форму """
        box_buttons.add_widget(self.button_sign_in)
        box_buttons.add_widget(self.button_registration)

        form_sign_in.add_widget(self.label_sign_in)
        form_sign_in.add_widget(label_enter_number)
        form_sign_in.add_widget(self.login_input)
        form_sign_in.add_widget(label_enter_password)
        form_sign_in.add_widget(self.password_input)
        form_sign_in.add_widget(box_buttons)
        form_sign_in.add_widget(self.label_password_invalid)

        self.add_widget(form_sign_in)

    def bind_callback_sign_in(self, func):
        self.button_sign_in.bind(on_press=func)

    def bind_callback_registration(self, func):
        self.button_registration.bind(on_press=func)


# Экран входа в учётныю запись
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login_screen'
        # Создадим форму авторизации
        self.login_form = LoginWidget(anchor_x="center", anchor_y="center")
        # Прикрепим к её кнопкам наши функции
        self.login_form.bind_callback_sign_in(self.callback_sign_in)
        self.login_form.bind_callback_registration(self.callback_registration)

        # Добавим на экран
        self.add_widget(self.login_form)

    def callback_sign_in(self, instance):
        login = self.login_form.login_input.text
        password = self.login_form.password_input.text

        # Попытка форматировать номер к виду +7...
        if len(login) > 0:
            if login[0] == '8':
                login = '+7' + login[1:]
            elif login[0] == '7':
                login = '+' + login

        # Попробуем авторизоваться и запишем ответ в лог
        log = backend.LoginUser(login, password)
        if log is True:
            # Если авторизация прошла успешно, то добавим файлы куки, чтобы потом повторно не входить.
            cookies_file = open('cookies', 'w')
            cookies_file.write(login)
            cookies_file.close()
            
            self.reset_screen()
            self.manager.transition.direction = 'left'
            self.manager.current = "menu_screen"
        else:
            self.login_form.label_password_invalid.text = "Неверный логин или пароль"

    def callback_registration(self, instance):
        self.reset_screen()
        self.manager.transition.direction = 'left'
        self.manager.current = "registration_screen"

    def reset_screen(self):
        self.login_form.login_input.text = ''
        self.login_form.password_input.text = ''
        self.login_form.label_password_invalid.text = ''
