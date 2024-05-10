import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Composite.composite import Leaf, Composite

class TestCompositePattern(unittest.TestCase):
    def test_composite(self):
        leaf = Leaf()
        composite = Composite()
        composite.add(leaf)
        self.assertEqual(composite.operation(), "Branch(Leaf)")

if __name__ == '__main__':
    unittest.main()
