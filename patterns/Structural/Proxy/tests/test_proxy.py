import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Proxy.proxy import Proxy, RealSubject

class TestProxyPattern(unittest.TestCase):
    def test_proxy_access(self):
        real_subject = RealSubject()
        proxy = Proxy(real_subject)
        # Capture the output using a StringIO object
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        proxy.request()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("RealSubject: Handling request.", output)
        self.assertIn("Proxy: Checking access prior to firing a real request.", output)

if __name__ == '__main__':
    unittest.main()
