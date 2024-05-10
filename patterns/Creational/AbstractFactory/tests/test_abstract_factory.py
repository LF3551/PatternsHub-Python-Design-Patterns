import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from AbstractFactory.abstract_factory import ConcreteFactory1, ProductA1, ProductB1


class TestAbstractFactory(unittest.TestCase):

    def test_product_a1_creation(self):
        factory = ConcreteFactory1()
        product = factory.create_product_a()
        self.assertIsInstance(product, ProductA1)

    def test_product_b1_creation(self):
        factory = ConcreteFactory1()
        product = factory.create_product_b()
        self.assertIsInstance(product, ProductB1)

if __name__ == '__main__':
    unittest.main()
