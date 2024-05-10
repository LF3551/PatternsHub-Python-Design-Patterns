import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Facade.facade import Facade, Subsystem1, Subsystem2

class TestFacadePattern(unittest.TestCase):
    def test_facade_operation(self):
        subsystem1 = Subsystem1()
        subsystem2 = Subsystem2()
        facade = Facade(subsystem1, subsystem2)
        self.assertIn("Subsystem1: Ready!", facade.operation())

if __name__ == '__main__':
    unittest.main()
