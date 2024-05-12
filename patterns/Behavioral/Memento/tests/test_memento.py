import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Memento.memento import Originator, Caretaker

class TestMementoPattern(unittest.TestCase):
    def test_memento(self):
        originator = Originator()
        caretaker = Caretaker()

        originator.set("State1")
        caretaker.add_memento(originator.save_to_memento())
        originator.set("State2")
        caretaker.add_memento(originator.save_to_memento())

        originator.restore_from_memento(caretaker.get_memento(0))
        self.assertEqual(originator._state, "State1")
        originator.restore_from_memento(caretaker.get_memento(1))
        self.assertEqual(originator._state, "State2")

if __name__ == '__main__':
    unittest.main()
