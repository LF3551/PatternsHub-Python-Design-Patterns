import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Mediator.mediator import ConcreteMediator, Component1, Component2

class TestMediatorPattern(unittest.TestCase):
    def test_mediator(self):
        c1 = Component1()
        c2 = Component2()
        mediator = ConcreteMediator(c1, c2)

        with self.assertLogs(level='INFO') as log:
            c1.do_a()
            self.assertIn('Component 1 does A.', log.output[0])
            self.assertIn('Mediator reacts on A and triggers following operations:', log.output[1])
            self.assertIn('Component 2 does C.', log.output[2])
            c2.do_d()
            self.assertIn('Component 2 does D.', log.output[3])
            self.assertIn('Mediator reacts on D and triggers following operations:', log.output[4])
            self.assertIn('Component 1 does B.', log.output[5])

if __name__ == '__main__':
    unittest.main()
