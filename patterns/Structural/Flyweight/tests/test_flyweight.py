import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Flyweight.flyweight import FlyweightFactory

class TestFlyweightPattern(unittest.TestCase):
    def test_flyweight_reuse(self):
        factory = FlyweightFactory([["Chevrolet", "Camaro2018", "pink"]])
        flyweight1 = factory.get_flyweight(["Chevrolet", "Camaro2018", "pink"])
        flyweight2 = factory.get_flyweight(["Chevrolet", "Camaro2018", "pink"])
        self.assertIs(flyweight1, flyweight2)

if __name__ == '__main__':
    unittest.main()
