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
import Backend.backend as backend


class UpperCurtainWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button_BACK = Button(text='Назад', size_hint_y=0.05)
        self.add_widget(self.button_BACK)

    def bind_callback_BACK(self, func):
        self.button_BACK.bind(on_press=func)


class RegistrationWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        form_registration = BoxLayout(orientation="vertical", size_hint=(.8, .4), spacing=3)

        self.label_registration = Label(text="Регистрация", color=Coffee_Colors[0], font_size=FontSize, size_hint=(1, 0.7))
        label_enter_number = Label(text="Введите номер:", color=Coffee_Colors[0], size_hint=(1, 0.3))
        self.login_input = TextInput(multiline=False, size_hint=(1, 0.7))
        label_enter_password1 = Label(text="Введите пароль:", color=Coffee_Colors[0], size_hint=(1, 0.3))
        self.password_input1 = TextInput(multiline=False, size_hint=(1, 0.7))
        label_enter_password2 = Label(text="Повторите пароль:", color=Coffee_Colors[0], size_hint=(1, 0.3))
        self.password_input2 = TextInput(multiline=False, size_hint=(1, 0.7))
        self.button_registration = Button(text="Регистрация", size_hint=(1, 0.7))
        # self.button_register.bind(on_press=self.reflex_button_register_press)
        self.label_error = Label(text="", color=(1, 0, 0, 1), font_size=FontSize, size_hint=(1, 0.7))

        form_registration.add_widget(self.label_registration)
        form_registration.add_widget(label_enter_number)
        form_registration.add_widget(self.login_input)
        form_registration.add_widget(label_enter_password1)
        form_registration.add_widget(self.password_input1)
        form_registration.add_widget(label_enter_password2)
        form_registration.add_widget(self.password_input2)
        form_registration.add_widget(self.button_registration)
        form_registration.add_widget(self.label_error)

        self.add_widget(form_registration)

    def bind_callback_registration(self, func):
        self.button_registration.bind(on_press=func)


class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'registration_screen'

        # Добавим верхнюю шторку
        self.UpperCurtain = UpperCurtainWidget(anchor_x='center', anchor_y='top')
        self.UpperCurtain.bind_callback_BACK(self.callback_BACK)
        self.add_widget(self.UpperCurtain)

        # И поле для регистрации
        self.registration_form = RegistrationWidget(anchor_x="center", anchor_y="center")
        self.registration_form.bind_callback_registration(self.callback_registration)
        self.add_widget(self.registration_form)

    def callback_BACK(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def callback_registration(self, instance):
        if self.registration_form.password_input1.text != self.registration_form.password_input2.text:
            self.registration_form.label_error.text = "Пароли не совпадают"
        elif self.registration_form.password_input1.text == '':
            self.registration_form.label_error.text = "Пароль не введён"
        else:
            number = self.registration_form.login_input.text
            password = self.registration_form.password_input1.text
            if 11 <= len(number) <= 12:

                # Попытка форматировать номер к виду +7...
                if len(number) > 0:
                    if number[0] == '8':
                        number = '+7' + number[1:]
                    elif number[0] == '7':
                        number = '+' + number

                log = backend.RegistrationUser(number, password)
                if log is True:
                    self.registration_form.label_error.text = ''
                    self.manager.transition.direction = 'right'
                    self.manager.current = "login_screen"
                else:
                    self.registration_form.label_error.text = "Пользователь с таким номером\nуже существует"
            else:
                self.registration_form.label_error.text = "Номер введён неправильно"
