__author__ = 'Kellan Childers'
from kivy.app import App
from kivy.uix.widget import Widget
from recipe import Recipe


class ShoppingList(Widget):
    def __init__(self, **kwargs):
        self.shopping_list = Recipe()
        super(ShoppingList, self).__init__(**kwargs)


class MainScreen(Widget):
    pass


class RecApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    RecApp().run()
