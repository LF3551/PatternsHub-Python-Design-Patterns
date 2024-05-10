import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Singleton.singleton import Singleton

class TestSingleton(unittest.TestCase):
    
    def test_singleton_instance(self):
        """Test that only one instance of Singleton is created."""
        instance1 = Singleton()
        instance2 = Singleton()
        self.assertIs(instance1, instance2)

    def test_singleton_business_logic(self):
        """Test the business logic method of Singleton."""
        instance = Singleton()
        self.assertIsNone(instance.some_business_logic())

if __name__ == '__main__':
    unittest.main()
