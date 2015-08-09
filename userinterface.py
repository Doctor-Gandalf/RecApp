__author__ = 'Kellan Childers'
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from recipe import Recipe

Builder.load_file('mainscreen.kv')
Builder.load_file('shoppingscreen.kv')
Builder.load_file('menus.kv')


class MainScreen(Widget):
    pass


class ShoppingList(BoxLayout):
    recipe = ObjectProperty(Recipe())
    list1 = ObjectProperty(None)

    class PopupInput(BoxLayout):
        pass

    def list_items(self):
        return [self.recipe.show_ingredient(item) for item in self.recipe]

    def add_item(self):
        popup_interior = self.PopupInput()

        popup_line_1 = BoxLayout(orientation="horizontal")
        popup_line_1.add_widget(Label(text="Input item name:"))
        popup_line_1.add_widget(TextInput(multiline=False))

        popup_line_2 = BoxLayout(orientation="horizontal")
        popup_line_2.add_widget(Label(text="Input item quantity:"))
        popup_line_2.add_widget(TextInput())

        popup_line_3 = BoxLayout(orientation="horizontal")
        popup_line_3.add_widget(Label(text="Input item qualifier:"))
        popup_line_3.add_widget(TextInput())

        popup_line_4 = SimpleButton(text="Enter")

        popup_interior.add_widget(popup_line_1)
        popup_interior.add_widget(popup_line_2)
        popup_interior.add_widget(popup_line_3)
        popup_interior.add_widget(popup_line_4)

        input_pop = Popup(title="Add item", content=popup_interior)
        input_pop.open()


    def add_recipe(self):
        pass

    def remove_item(self):
        pass

    def save_recipe(self):
        pass

    def save_list(self):
        pass

    def remove_recipe(self):
        pass

    def load_recipe(self):
        pass

    def load_list(self):
        pass

    def clear(self):
        self.recipe.clear()


class MenuBar(BoxLayout):
    pass


class TopMenu(MenuBar):
    pass


class BottomMenu(MenuBar):
    pass


class SimpleButton(Button):
    pass
