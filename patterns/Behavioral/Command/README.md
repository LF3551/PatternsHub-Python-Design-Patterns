# Command Pattern 📋

## Overview 📖
The Command Pattern turns a request into a stand-alone object that contains all information about the request. This transformation allows command-based operations like issuing requests, queuing them, logging them, and implementing undo capabilities.

## Use Cases 🔍
- **Undo Functionality**: Commands can store state for reversing its effects, enabling robust undo capabilities.
- **Queueing Operations**: Commands can be queued and executed at different times.
- **Operations Logging**: All actions can be logged and stored as commands, which helps in auditing and replaying sequences of operations.

## Implementation 🛠️
The `command.py` file typically includes:
- An `ICommand` interface, which defines the method for executing commands.
- Concrete command classes that implement the `ICommand` interface to execute specific actions.
- A `Invoker` class that invokes commands by calling the execute method.
- A `Receiver` class which knows how to perform the operations.

## Example Usage 📝
```python
class Light:
    def turn_on(self):
        print("The light is on")

    def turn_off(self):
        print("The light is off")

class ICommand:
    def execute(self):
        pass

class TurnOnCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()

class TurnOffCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()

class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def press_button(self):
        self._command.execute()

# Example usage
light = Light()
turn_on_command = TurnOnCommand(light)
remote = RemoteControl()
remote.set_command(turn_on_command)
remote.press_button()
```
## Output 📊
```python
The light is on
```

This output demonstrates the remote control turning on the light via the Command Pattern.



## Business Logic Method 🧠
The Command Pattern can be expanded to handle complex business logic by integrating with other patterns or systems. This allows the pattern to be dynamically adaptable to varying business rules and workflows.

For example, commands can be combined with the Strategy Pattern to change the algorithm used at runtime, or with the Observer Pattern to notify other parts of the system when commands are executed.

```python
class CommandWithStrategy(ICommand):
    def __init__(self, receiver, strategy):
        self._receiver = receiver
        self._strategy = strategy

    def execute(self):
        print("Executing command with strategy.")
        self._strategy.execute(self._receiver)

class SampleStrategy:
    def execute(self, receiver):
        receiver.perform_action()

class Receiver:
    def perform_action(self):
        print("Receiver is performing action.")
```
## Testing 🧪

The test_command.py file should contain tests for:

- Ensuring that the right commands trigger the correct actions.
- Verifying that the undo functionality works as expected.
- Checking the integrity and order of queued commands.