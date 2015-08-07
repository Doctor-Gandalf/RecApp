__author__ = 'Kellan Childers'
from kivy.app import App
from kivy.uix.widget import Widget
from recipe import Recipe


class ShoppingList(Widget):
    def __init__(self, **kwargs):
        self.recipe = Recipe()
        super(ShoppingList, self).__init__(**kwargs)

    def list_items(self):
        return_string = ""
        for item in self.recipe:
            return_string = return_string + '\n' + self.recipe.show_ingredient(item)
        return return_string


class MainScreen(Widget):
    pass


class RecApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    RecApp().run()
