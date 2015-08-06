__author__ = 'Kellan Childers'
from kivy.uix.widget import Widget
from kivy.app import App


class ShoppingList(Widget):
    pass


class RecApp(App):
    def build(self):
        return ShoppingList()

if __name__ == "__main__":
    RecApp().run()
