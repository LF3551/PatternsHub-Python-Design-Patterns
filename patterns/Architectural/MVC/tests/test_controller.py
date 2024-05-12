import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from unittest.mock import patch
from MVC.Controller.controller import Controller

class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    @patch('MVC.Controller.controller.display_item')
    def test_add_item(self, mock_display):
        self.controller.add_item('test', 'value')
        mock_display.assert_called_with('test', 'value')

    @patch('MVC.Controller.controller.display_error')
    def test_add_existing_item(self, mock_display):
        self.controller.add_item('test', 'value')  # Первый вызов, создание элемента
        self.controller.add_item('test', 'value')  # Второй вызов, элемент уже существует
        mock_display.assert_called_with('Item already exists')

if __name__ == '__main__':
    unittest.main()

