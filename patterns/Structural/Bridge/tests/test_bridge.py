import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Bridge.bridge import ConcreteImplementorA, ConcreteImplementorB, RefinedAbstraction

class TestBridgePattern(unittest.TestCase):
    def test_bridge_functionality(self):
        implementor_a = ConcreteImplementorA()
        abstraction = RefinedAbstraction(implementor_a)
        self.assertIn("ConcreteImplementorA", abstraction.operation())

        implementor_b = ConcreteImplementorB()
        abstraction.implementor = implementor_b
        self.assertIn("ConcreteImplementorB", abstraction.operation())

if __name__ == '__main__':
    unittest.main()
