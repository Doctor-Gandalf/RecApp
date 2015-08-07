__author__ = 'Kellan Childers'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MainScreen(Widget):
    pass


class ShoppingList  (BoxLayout):
    shopping_list = ObjectProperty(None)
    pass


class RecApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    RecApp().run()
