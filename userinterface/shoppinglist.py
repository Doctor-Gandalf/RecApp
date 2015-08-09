__author__ = 'Kellan Childers'
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from menus import SimpleButton
from recipe import Recipe
Builder.load_file('userinterface/shoppinglist.kv')


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
        line_1_text = TextInput()
        popup_line_1.add_widget(line_1_text)

        popup_line_2 = BoxLayout(orientation="horizontal")
        popup_line_2.add_widget(Label(text="Input item quantity:"))
        line_2_text = TextInput()
        popup_line_2.add_widget(line_2_text)

        popup_line_3 = BoxLayout(orientation="horizontal")
        popup_line_3.add_widget(Label(text="Input item qualifier:"))
        line_3_text = TextInput()
        popup_line_3.add_widget(line_3_text)

        popup_line_4 = SimpleButton(text="Enter")

        popup_interior.add_widget(popup_line_1)
        popup_interior.add_widget(popup_line_2)
        popup_interior.add_widget(popup_line_3)
        popup_interior.add_widget(popup_line_4)

        input_pop = Popup(title="Add item", content=popup_interior)
        input_pop.open()

        item_name = line_1_text.text
        item_quantity = line_2_text.text
        item_qualifier = line_3_text.text

        self.recipe.add_ingredient(item_name, item_quantity, item_qualifier)

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
