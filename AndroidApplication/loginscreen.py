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

from global_settings import *


# Виджет входа
class LoginWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        form_sign_in = BoxLayout(orientation="vertical", size_hint=(.8, .4), spacing=3)

        self.label_sign_in = Label(text="Вход", color=Coffee_Colors[0], font_size=FontSize, size_hint=(1, 0.7))
        label_enter_number = Label(text="Номер:", color=Coffee_Colors[0], size_hint=(1, 0.3))
        ''' Ввод номера телефона '''
        self.login_input = TextInput(multiline=False, size_hint=(1, 0.7))
        label_enter_password = Label(text="Пароль:", color=Coffee_Colors[0], size_hint=(1, 0.3))
        ''' Ввод пароля '''
        self.password_input = TextInput(multiline=False, size_hint=(1, 0.7))
        box_buttons = BoxLayout(size_hint=(1, 0.7))
        self.button_sign_in = Button(text="Войти", size_hint=(.65, 1))
        self.button_register = Button(text="Регистрация", size_hint=(.35, 1))

        '''
            Текст об ошибке при входе.
            Изначально пустой текст.
        '''
        self.label_password_invalid = Label(text="", color=(1, 0, 0, 1), font_size=FontSize, size_hint=(1, 0.7))

        """ Добавляем виджеты в форму """
        box_buttons.add_widget(self.button_sign_in)
        box_buttons.add_widget(self.button_register)

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

    def bind_callback_registry(self, func):
        self.button_register.bind(on_press=func)


# Экран входа в учётныю запись
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login_screen'
        # Создадим форму авторизации
        self.login_form = LoginWidget(anchor_x="center", anchor_y="center")
        # Прикрепим к её кнопкам наши функции
        self.login_form.bind_callback_sign_in(self.callback_sign_in)
        self.login_form.bind_callback_registry(self.callback_registry)

        # Добавим на экран
        self.add_widget(self.login_form)

    def callback_sign_in(self, instance):
        print('Sign in')

    def callback_registry(self, instance):
        print('Registry')
