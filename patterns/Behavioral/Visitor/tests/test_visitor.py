import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Visitor.visitor import ConcreteElementA, ConcreteElementB, ConcreteVisitor1, ConcreteVisitor2

class TestVisitorPattern(unittest.TestCase):
    def test_visitor(self):
        element_a = ConcreteElementA()
        element_b = ConcreteElementB()
        visitor1 = ConcreteVisitor1()
        visitor2 = ConcreteVisitor2()

        with self.assertLogs(level='INFO') as log:
            element_a.accept(visitor1)
            element_b.accept(visitor1)
            element_a.accept(visitor2)
            element_b.accept(visitor2)

            # Проверяем только сообщения о действиях посетителей
            self.assertTrue(any('ConcreteVisitor1 is processing ConcreteElementA' in message for message in log.output))
            self.assertTrue(any('ConcreteVisitor1 is processing ConcreteElementB' in message for message in log.output))
            self.assertTrue(any('ConcreteVisitor2 is processing ConcreteElementA' in message for message in log.output))
            self.assertTrue(any('ConcreteVisitor2 is processing ConcreteElementB' in message for message in log.output))

if __name__ == '__main__':
    unittest.main()
