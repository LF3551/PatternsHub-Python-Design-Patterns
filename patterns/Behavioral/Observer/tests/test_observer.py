import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Observer.observer import Subject, ConcreteObserverA, ConcreteObserverB

class TestObserverPattern(unittest.TestCase):
    def test_updates(self):
        subject = Subject()
        observer_a = ConcreteObserverA()
        observer_b = ConcreteObserverB()
        subject.attach(observer_a)
        subject.attach(observer_b)

        # Убедитесь, что проверяете весь текст лога, включая префикс уровня логирования и 'root'.
        with self.assertLogs(level='INFO') as log:
            subject.notify()
            self.assertIn('INFO:root:ConcreteObserverA: Received an update!', log.output)
            self.assertIn('INFO:root:ConcreteObserverB: Received an update!', log.output)

if __name__ == '__main__':
    unittest.main()