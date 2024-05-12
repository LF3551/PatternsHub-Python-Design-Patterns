import logging

class Command:
    def execute(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Light:
    """ Receiver class """
    def turn_on(self):
        logging.info("The light is on")
        
    def turn_off(self):
        logging.info("The light is off")

class TurnOnCommand(Command):
    """ Concrete command to turn on the light """
    def __init__(self, light):
        self._light = light
    
    def execute(self):
        self._light.turn_on()

class TurnOffCommand(Command):
    """ Concrete command to turn off the light """
    def __init__(self, light):
        self._light = light
    
    def execute(self):
        self._light.turn_off()

class RemoteControl:
    """ Invoker class """
    def submit(self, command):
        command.execute()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    light = Light()
    turn_on = TurnOnCommand(light)
    turn_off = TurnOffCommand(light)
    remote = RemoteControl()

    remote.submit(turn_on)
    remote.submit(turn_off)
