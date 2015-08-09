__author__ = 'Kellan Childers'
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
Builder.load_file('menus.kv')


class MenuBar(BoxLayout):
    pass


class TopMenu(MenuBar):
    pass


class BottomMenu(MenuBar):
    pass


class SimpleButton(Button):
    pass
