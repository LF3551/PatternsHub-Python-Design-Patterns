import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Builder.builder import ConcreteBuilder, Director

class TestBuilderPattern(unittest.TestCase):
    def test_product_construction(self):
        builder = ConcreteBuilder()
        director = Director(builder)
        director.construct()
        product = builder.get_result()
        self.assertEqual(product, ['Part A', 'Part B'])

if __name__ == '__main__':
    unittest.main()
