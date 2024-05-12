import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from EventDriven.event_driven import EventManager, EmailNotificationListener, LoggingListener

class TestEventDrivenPattern(unittest.TestCase):
    @patch('EventDriven.event_driven.logging')
    def test_event_driven(self, mock_logging):
        manager = EventManager()
        email_listener = EmailNotificationListener()
        logging_listener = LoggingListener()

        manager.subscribe("order_placed", email_listener)
        manager.subscribe("order_placed", logging_listener)

        manager.notify("order_placed", "Order #1234 has been placed")
        manager.notify("order_placed", "Order #1235 has been placed")

        self.assertEqual(mock_logging.info.call_count, 8)

if __name__ == '__main__':
    unittest.main()

