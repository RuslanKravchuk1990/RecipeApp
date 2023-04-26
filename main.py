# libraries
from io import BytesIO
# from PIL import Image, ImageTK
from py_edamam import PyEdamam
import requests
import tkinter as tk
import webbrowser

WINDOW_TITLE = 'Recipe App'
RECIPE_IMAGE_WIDTH = 350
RECIPE_IMAGE_HEIGHT = 300

class RecipeApp(object):

    def __init__(self, recipe_app_id, recipe_app_key):
        self.recipe_app_id = recipe_app_id
        self.recipe_app_key = recipe_app_key
        self.window = tk.Tk()

        self.window.geometry("")
        self.window.configure(bg="#fcdada")
        self.window.title(WINDOW_TITLE)

        self.search_lebel = tk.Label(self.window, text="Search Recipe", bg="#5c969e")
        self.search_label.grid(column = 0, row = 0, padx = 5)

        self.search_entry = tk.Entry(master = self.window, width = 40)
        self.search_entry.grid(column = 1, row = 0, padx = 5, pady = 10)

        self.search_button = tk.Button(self.window, text = "search", highlightbackground = "#ea86b6",
            command = self.__run_search_query)
        self.search_button.grid(column = 2, row = 0, padx = 5)

    def __run_search_query(self):
        pass

    def __get_recipe(self, query):
        pass

    def __show_image(self, image_url):
        pass

    def __get_ingredients(self, recipe):
        pass

    def run_app(self):
        self.window.mainloop()

if __name__ == "__main__":
    APP_ID = ""
    APP_KEY = ""

    recipe_app = RecipeApp(APP_ID, APP_KEY)
    recipe_app.run()