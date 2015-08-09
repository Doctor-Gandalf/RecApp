__author__ = 'Kellan Childers'
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

# Load the kvlang file associated with this file.
Builder.load_file('userinterface/menus.kv')


class MenuBar(BoxLayout):
    """Placeholder to assist formatting of all menus in application."""
    pass


class TopMenu(MenuBar):
    """Placeholder to assist formatting top menu bar."""
    pass


class BottomMenu(MenuBar):
    """Placeholder to assist formatting bottom menu bar."""
    pass


class SimpleButton(Button):
    """Placeholder to assist formatting all buttons in application."""
    pass
