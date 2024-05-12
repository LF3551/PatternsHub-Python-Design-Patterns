import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Strategy.strategy import Context, ConcreteStrategyA, ConcreteStrategyB

class TestStrategyPattern(unittest.TestCase):
    def test_strategy_execution(self):
        context = Context(ConcreteStrategyA())
        with self.assertLogs(level='INFO') as log:
            context.do_some_logic()
            self.assertTrue(any('Executing strategy A' in message for message in log.output))
        context.set_strategy(ConcreteStrategyB())
        with self.assertLogs(level='INFO') as log:
            context.do_some_logic()
            self.assertTrue(any('Executing strategy B' in message for message in log.output))

if __name__ == '__main__':
    unittest.main()
