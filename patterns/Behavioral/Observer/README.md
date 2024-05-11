# Observer Pattern 📡

## Overview 📖
The Observer Pattern is a behavioral design pattern that establishes a one-to-many relationship between objects. A single object, known as the subject, maintains a list of its dependents, known as observers, and notifies them automatically of any state changes.

## Use Cases 🔍
- **User Interface Updates**: Automatically update the user interface in response to changes in underlying data.
- **Event Notification Systems**: Notify different systems or components of changes in state or specific events that they need to react to.
- **Cross-module Communication**: Facilitate communication between different modules or services in a loosely coupled manner.

## Implementation 🛠️
The `Observer` pattern is implemented in its own subdirectory within this repository:

`observer.py`: Contains the core interfaces and classes for the Observer pattern, including the Subject class and Observer interface.
`concrete_observer.py` Implements specific observers that react to notifications from the Subject.

## Example Usage 📝
```python
# In observer.py
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        raise NotImplementedError("Observer subclasses must implement this method.")

# In concrete_observer.py
class ConcreteObserverA(Observer):
    def update(self):
        print("ConcreteObserverA: Notified of the change!")

class ConcreteObserverB(Observer):
    def update(self):
        print("ConcreteObserverB: Notified of the change!")

if __name__ == "__main__":
    subject = Subject()
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()
    subject.attach(observer_a)
    subject.attach(observer_b)
    subject.notify()

```
## Output 📊
```python
ConcreteObserverA: Notified of the change!
ConcreteObserverB: Notified of the change!
```
This output illustrates how each observer reacts to the notification from the subject, demonstrating the real-time communication and update mechanism within the Observer pattern.

## Business Logic Method 🧠

The Observer Pattern can be extended to incorporate more sophisticated interaction scenarios, such as filtering notifications based on the observer's state or the type of update. Here’s an example of how a more complex scenario could be handled:

```python
class FilteredObserver(Observer):
    def __init__(self, state_interest):
        self._state_interest = state_interest

    def update(self, state):
        if state == self._state_interest:
            print(f"FilteredObserver: Notified of the change to {state} state!")

if __name__ == "__main__":
    subject = Subject()
    observer_a = ConcreteObserverA()
    observer_filtered = FilteredObserver("specific_state")
    subject.attach(observer_a)
    subject.attach(observer_filtered)
    subject.notify_state_change("specific_state")

```

## Testing 🧪
Run the test suite in the tests/ directory to verify that the Observer pattern is implemented correctly and behaves as expected. This helps ensure that subjects properly manage their list of observers and trigger updates accurately.