import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from MVC.Model.model import DataModel
from MVC.View.view import display_item, display_error

class Controller:
    def __init__(self):
        self.model = DataModel()

    def add_item(self, key, value):
        if key in self.model.data:
            display_error("Item already exists")
        else:
            item = self.model.add_item(key, value)
            display_item(key, item)
            return item

    def get_item(self, key):
        item = self.model.get_item(key)
        if item is None:
            display_error("Item not found")
        else:
            display_item(key, item)
        return item
