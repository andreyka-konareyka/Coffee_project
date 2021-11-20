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
from kivy.core.window import Window


# Виджет входа
class LoginWidget(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text="login", size_hint=[0.8, 0.4]))


# Экран входа в учётныю запись
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login_screen'
        self.add_widget(LoginWidget(anchor_x="center", anchor_y="center"))