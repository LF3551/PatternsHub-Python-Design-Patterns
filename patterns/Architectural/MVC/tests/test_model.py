import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from MVC.Model.model import DataModel

class TestDataModel(unittest.TestCase):
    def setUp(self):
        self.model = DataModel()

    def test_add_item(self):
        result = self.model.add_item('test', 'value')
        self.assertEqual(result, 'value')

    def test_get_item(self):
        self.model.add_item('test', 'value')
        result = self.model.get_item('test')
        self.assertEqual(result, 'value')

if __name__ == '__main__':
    unittest.main()
