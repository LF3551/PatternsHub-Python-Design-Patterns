import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Decorator.decorator import ConcreteComponent, ConcreteDecoratorA, ConcreteDecoratorB

class TestDecoratorPattern(unittest.TestCase):
    def test_decorator(self):
        simple = ConcreteComponent()
        decorated = ConcreteDecoratorA(simple)
        more_decorated = ConcreteDecoratorB(decorated)
        self.assertEqual(more_decorated.operation(), "ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))")

if __name__ == '__main__':
    unittest.main()
