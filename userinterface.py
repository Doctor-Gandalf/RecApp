__author__ = 'Kellan Childers'
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from recipe import Recipe


Builder.load_file('userinterface.kv')


class MainScreen(Widget):
    pass


class ShoppingList(Widget):
    recipe = ObjectProperty(Recipe())

    def list_items(self):
        return [self.recipe.show_ingredient(item) for item in self.recipe]


class MenuBar(BoxLayout):
    pass


class TopMenu(MenuBar):
    pass


class BottomMenu(MenuBar):
    class SimpleButton(Button):
        pass
