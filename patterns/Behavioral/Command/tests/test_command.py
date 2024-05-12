import unittest
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Command.command import Light, TurnOnCommand, TurnOffCommand, RemoteControl

class TestCommandPattern(unittest.TestCase):
    @patch('Command.command.logging')
    def test_command(self, mock_logging):
        light = Light()
        turn_on = TurnOnCommand(light)
        turn_off = TurnOffCommand(light)
        remote = RemoteControl()

        remote.submit(turn_on)
        mock_logging.info.assert_called_with("The light is on")
        
        remote.submit(turn_off)
        mock_logging.info.assert_called_with("The light is off")

if __name__ == '__main__':
    unittest.main()
