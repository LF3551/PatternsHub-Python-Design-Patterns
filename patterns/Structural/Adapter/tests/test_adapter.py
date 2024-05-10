import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Adapter.adapter import Adapter, Adaptee

class TestAdapterPattern(unittest.TestCase):
    def test_adapter_provides_translation(self):
        adaptee = Adaptee()
        adapter = Adapter()
        expected_translation = f"Adapter: (TRANSLATED) {adaptee.specific_request()[::-1]}"
        self.assertEqual(adapter.request(), expected_translation)

if __name__ == '__main__':
    unittest.main()