# libraries
from io import BytesIO
from PIL import Image, ImageTK
from py_edamam import PyEdamam
import requests
import tkinter as tk
import webbrowser

WINDOW_TITLE = 'Recipe App'
RECIPE_IMAGE_WIDTH = 350
RECIPE_IMAGE_HEIGHT = 300

class RecipeApp(object);

    def __init__(self, recipe_app_id, recipe_app_key)
        self.recipe_app_id = recipe_app_id
        self.recipe_app_key = recipe_app_key
        self.window = tk.Tk()

        self.window.geometry("")
        self.window.configure(bg="#fcdada")
        self.window.title(WINDOW_TITLE)

        self.search_lebel = tk.Label(self.window, text="Search Recipe", bg="#5c969e")
        self.search_label.grid(column = 0, row = 0, padx = 5)

    def __get_recipe(self, query):
        pass

    def __show_image(self, image_url)
