import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Prototype.prototype import ConcretePrototype1

class TestPrototypePattern(unittest.TestCase):
    def test_prototype_clone(self):
        prototype_original = ConcretePrototype1(1001)
        prototype_clone = prototype_original.clone()
        self.assertEqual(str(prototype_original), str(prototype_clone))

if __name__ == '__main__':
    unittest.main()
