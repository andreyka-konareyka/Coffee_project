from kivy.app import App
from kivy.config import Config
Config.set("graphics", "width", 640)    # Установка разрешения, похожего не телефон
Config.set("graphics", "height", 960)   # Нужно для отладки на ПК

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


class TestScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'test_screen'
        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        layout.add_widget(Button(text="Test button", size_hint=[0.8, 0.2]))

        self.add_widget(layout)


class CoffeeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TestScreen())
        return sm


if __name__ == '__main__':
    CoffeeApp().run()
