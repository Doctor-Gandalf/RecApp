__author__ = 'Kellan Childers'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from recipe import Recipe


class ShoppingList(Widget):
    def __init__(self, **kwargs):
        self.recipe = Recipe()
        super(ShoppingList, self).__init__(**kwargs)

    def list_items(self):
        return [self.recipe.show_ingredient(item) for item in self.recipe]


class SimpleButton(Button):
    pass


class MainScreen(Widget):
    pass


class RecApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    RecApp().run()
