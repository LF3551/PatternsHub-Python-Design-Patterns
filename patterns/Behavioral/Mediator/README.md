# [Mediator Pattern](../) 🕊️

## Overview 📖
The Mediator Pattern simplifies complex communication between multiple objects or classes by introducing a single mediator object that handles all the communication and control between related objects. By doing so, it decreases the direct references among objects, thereby reducing dependencies and facilitating easier maintenance and modification of interactions.

## Use Cases 🔍
- **User Interface Control**: Centralize complex communications between various GUI components into a single mediator object.
- **Chat Rooms**: Facilitate the communication between multiple users through a single central server acting as the mediator.
- **System Workflow**: Manage complex logic and dependencies between different components of a system, simplifying the workflow through centralized control.

## Implementation 🛠️
The `mediator.py` file generally includes:
- A `Mediator` interface with methods for sending messages from components and notifying changes.
- Concrete `Mediator` class implementing the Mediator interface to coordinate complex interactions.
- A `Component` base class that maintains a reference to the mediator object.
- Concrete `Component` classes that interact with each other through the mediator.

## Example Usage 📝
```python
class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self.component1 = Component1(self)
        self.component2 = Component2(self)

    def notify(self, sender, event):
        if event == 'A':
            print("Mediator reacts on A and triggers following operations:")
            self.component2.do_c()
        elif event == 'D':
            print("Mediator reacts on D and triggers following operations:")
            self.component1.do_b()

class Component1:
    def __init__(self, mediator):
        self._mediator = mediator

    def do_a(self):
        print("Component 1 does A.")
        self._mediator.notify(self, 'A')

    def do_b(self):
        print("Component 1 does B.")

class Component2:
    def __init__(self, mediator):
        self._mediator = mediator

    def do_c(self):
        print("Component 2 does C.")

    def do_d(self):
        print("Component 2 does D.")
        self._mediator.notify(self, 'D')

# Example usage
mediator = ConcreteMediator()
component1 = mediator.component1
component2 = mediator.component2

component1.do_a()
component2.do_d()
```
## Output 📊
```python
Component 1 does A.
Mediator reacts on A and triggers following operations:
Component 2 does C.
Component 2 does D.
Mediator reacts on D and triggers following operations:
Component 1 does B.

```

This output shows the mediator facilitating and handling interactions between two components, coordinating their actions based on the events that occur.



## Business Logic Method 🧠
Mediator can manage complex dependencies within larger systems, making it easier to change the system's interaction by simply changing the mediator without altering the actual components:

```python
# Additional logic can be embedded into mediator to handle more complex scenarios
def notify(self, sender, event):
    if event == 'A':
        # Complex logic before triggering component
        print("Preparing environment for Component 2 action C.")
        self.component2.do_c()


```

## Testing 🧪
The test_mediator.py file should contain tests ensuring:

- Correct propagation of actions among components via the mediator.
- Proper handling and modification of component interactions without direct dependencies.