import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from unittest.mock import patch
from P2P.peer import Peer

class TestPeer(unittest.TestCase):
    @patch('socket.socket.connect')
    def test_connect_to_peer(self, mock_connect):
        peer = Peer('localhost', 5000)
        peer.connect_to_peer('localhost', 5001)
        mock_connect.assert_called_with(('localhost', 5001))

if __name__ == '__main__':
    unittest.main()
