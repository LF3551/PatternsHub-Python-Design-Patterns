import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from unittest.mock import patch
from MVC.View.view import display_item, display_error

class TestView(unittest.TestCase):
    @patch('builtins.print')
    def test_display_item(self, mock_print):
        display_item("test", "value")
        mock_print.assert_called_with("test: value")

    @patch('builtins.print')
    def test_display_error(self, mock_print):
        display_error("An error occurred")
        mock_print.assert_called_with("Error: An error occurred")

if __name__ == '__main__':
    unittest.main()
