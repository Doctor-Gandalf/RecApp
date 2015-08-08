__author__ = 'Kellan Childers'
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from recipe import Recipe


class MainScreen(Widget):
    pass


class ShoppingList(Widget):
    def __init__(self, **kwargs):
        self.recipe = Recipe()
        super(ShoppingList, self).__init__(**kwargs)

    def list_items(self):
        return [self.recipe.show_ingredient(item) for item in self.recipe]


class MenuBar(BoxLayout):
    class SimpleButton(Button):
        pass
