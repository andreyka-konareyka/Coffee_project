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


class UpperCurtainWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text='Назад', size_hint_y=0.05))


class RegistryWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        form_sign_in = BoxLayout(orientation="vertical", size_hint=(.8, .4), spacing=3)

        self.label_sign_in = Label(text="Регистрация", color=Coffee_Colors[0], font_size=FontSize, size_hint=(1, 0.7))
        label_enter_number = Label(text="Введите номер:", color=Coffee_Colors[0], size_hint=(1, 0.3))
        self.login_input = TextInput(multiline=False, size_hint=(1, 0.7))
        label_enter_password1 = Label(text="Введите пароль:", color=Coffee_Colors[0], size_hint=(1, 0.3))
        self.password_input1 = TextInput(multiline=False, size_hint=(1, 0.7))
        label_enter_password2 = Label(text="Повторите пароль:", color=Coffee_Colors[0], size_hint=(1, 0.3))
        self.password_input2 = TextInput(multiline=False, size_hint=(1, 0.7))
        self.button_register = Button(text="Регистрация", size_hint=(1, 0.7))
        # self.button_register.bind(on_press=self.reflex_button_register_press)
        self.label_error = Label(text="", color=(1, 0, 0, 1), font_size=FontSize, size_hint=(1, 0.7))

        form_sign_in.add_widget(self.label_sign_in)
        form_sign_in.add_widget(label_enter_number)
        form_sign_in.add_widget(self.login_input)
        form_sign_in.add_widget(label_enter_password1)
        form_sign_in.add_widget(self.password_input1)
        form_sign_in.add_widget(label_enter_password2)
        form_sign_in.add_widget(self.password_input2)
        form_sign_in.add_widget(self.button_register)
        form_sign_in.add_widget(self.label_error)

        self.add_widget(form_sign_in)


class RegistryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'registry_screen'
        self.add_widget(UpperCurtainWidget(anchor_x='center', anchor_y='top'))
        self.add_widget(RegistryWidget(anchor_x="center", anchor_y="center"))
