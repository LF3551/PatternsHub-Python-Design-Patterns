import unittest
import sys
import os
from io import StringIO
import contextlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from ChainOfResponsibility.chainofresponsibility import ConcreteHandler1, ConcreteHandler2, DefaultHandler

class TestChainOfResponsibilityPattern(unittest.TestCase):
    def test_chain_of_responsibility(self):
        h1 = ConcreteHandler1()
        h2 = ConcreteHandler2(DefaultHandler())
        h1.set_successor(h2)

        requests = [2, 14, 22, 5, 17]
        outputs = []

        with contextlib.redirect_stdout(StringIO()) as f:
            for request in requests:
                h1.handle(request)
            outputs = f.getvalue().strip().split("\n")

        self.assertEqual(outputs, [
            'Handler 1 is handling request 2',
            'Handler 2 is handling request 14',
            'Default handler for request 22',
            'Handler 1 is handling request 5',
            'Handler 2 is handling request 17'
        ])

if __name__ == '__main__':
    unittest.main()
