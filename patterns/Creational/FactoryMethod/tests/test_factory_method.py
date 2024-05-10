import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from FactoryMethod.factory_method import ConcreteCreator, Product

class TestFactoryMethod(unittest.TestCase):
    
    def test_product_instance(self):
        """Test that a ConcreteProduct instance is created."""
        creator = ConcreteCreator()
        product = creator.factory_method()
        self.assertTrue(isinstance(product, Product))

    def test_product_operation(self):
        """Test the operation method of a product."""
        creator = ConcreteCreator()
        self.assertEqual(creator.operation(), "Result of the ConcreteProduct operation.")

if __name__ == '__main__':
    unittest.main()
