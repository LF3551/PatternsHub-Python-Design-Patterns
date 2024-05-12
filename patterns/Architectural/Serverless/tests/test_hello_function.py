import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from unittest.mock import patch
from Serverless.hello_function import lambda_handler

class TestHelloFunction(unittest.TestCase):
    def test_lambda_handler(self):
        event = {}  
        context = {}  
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn("Hello from Lambda!", response['body'])

if __name__ == '__main__':
    unittest.main()
