import unittest
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from CQRS.cqrs import Store, AddItemCommand, GetAllItemsQuery, CQRS

class TestCQRSPattern(unittest.TestCase):
    @patch('CQRS.cqrs.logging')
    def test_cqrs(self, mock_logging):
        store = Store()
        cqrs = CQRS()

        # Test commands
        cqrs.dispatch(AddItemCommand(store, "Apple"))
        mock_logging.info.assert_called_with("Added item: Apple")
        
        # Test queries
        items = cqrs.dispatch(GetAllItemsQuery(store))
        self.assertEqual(items, ["Apple"])

if __name__ == '__main__':
    unittest.main()
