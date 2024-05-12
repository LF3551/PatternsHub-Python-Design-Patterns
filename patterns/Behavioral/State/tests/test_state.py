import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from State.state import Context, ConcreteStateA, ConcreteStateB

class TestStatePattern(unittest.TestCase):
    def test_state_transition(self):
        context = Context(ConcreteStateA())
        self.assertIsInstance(context.state, ConcreteStateA)
        context.request()
        self.assertIsInstance(context.state, ConcreteStateB)
        context.request()
        self.assertIsInstance(context.state, ConcreteStateA)

if __name__ == '__main__':
    unittest.main()
