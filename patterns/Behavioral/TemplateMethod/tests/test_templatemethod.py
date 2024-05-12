import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from TemplateMethod.templatemethod import ConcreteClassA, ConcreteClassB

class TestTemplateMethodPattern(unittest.TestCase):
    def test_concrete_class_a(self):
        instance = ConcreteClassA()
        with self.assertLogs(level='INFO') as log:
            instance.template_method()
            # Проверяем, что основные и специфические действия класса А вызывались
            self.assertIn('I am doing the bulk of the work', log.output[0])
            self.assertIn('Implemented Operation1', log.output[1])

    def test_concrete_class_b(self):
        instance = ConcreteClassB()
        with self.assertLogs(level='INFO') as log:
            instance.template_method()
            # Проверяем, что все методы, включая переопределенный хук, вызывались
            self.assertIn('I am doing the bulk of the work', log.output[0])
            self.assertIn('Implemented Operation2', log.output[1])
            self.assertIn('Overridden Hook', log.output[2])

if __name__ == '__main__':
    unittest.main()
