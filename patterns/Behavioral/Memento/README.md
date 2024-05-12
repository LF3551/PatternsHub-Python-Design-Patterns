# [Memento Pattern](../) 💾

## Overview 📖
The Memento Pattern provides the ability to capture and externalize an object's internal state without violating encapsulation, so that the object can be returned to this state later. It is particularly useful for implementing rollback, undo, or snapshot capabilities in applications.

## Use Cases 🔍
- **Undo Mechanisms**: Allows users to undo changes to the state of an object to a previous state.
- **Snapshots**: Captures the state of an object at a particular time and restores it when necessary, useful in scenarios like save points in games or transaction rollbacks in databases.
- **State Auditing**: Stores historical states of an object for auditing or tracking purposes over time.

## Implementation 🛠️
The `memento.py` file usually includes:
- A `Memento` class to store the state of the `Originator`.
- An `Originator` class, which creates a memento containing a snapshot of its current internal state and uses the memento to restore its internal state.
- A `Caretaker` class, which is responsible for keeping track of the memento. The caretaker requests a save from the originator to capture the current state and uses the memento returned to restore the state of the originator.

## Example Usage 📝
```python
class Memento:
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state):
        print(f"Setting state to {state}")
        self._state = state

    def save_to_memento(self):
        print(f"Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()
        print(f"State after restoring from Memento: {self._state}")

class Caretaker:
    def __init__(self):
        self._saved_states = []

    def add_memento(self, memento):
        self._saved_states.append(memento)

    def get_memento(self, index):
        return self._saved_states[index]

# Example usage
originator = Originator()
caretaker = Caretaker()

originator.set_state("State1")
caretaker.add_memento(originator.save_to_memento())

originator.set_state("State2")
caretaker.add_memento(originator.save_to_memento())

originator.restore_from_memento(caretaker.get_memento(0))

```
## Output 📊
```python
Setting state to State1
Saving to Memento.
Setting state to State2
Saving to Memento.
State after restoring from Memento: State1

```
This output demonstrates how the state of the Originator is saved and restored using Mementos managed by the Caretaker.



## Business Logic Method 🧠
The Memento pattern can be extended to include more complex state serialization, or integration with database systems for persistent state saving:

```python
# Enhanced Memento with serialization for complex state management.
class SerializableMemento(Memento):
    def serialize(self):
        # Serialization logic to convert state to a storable format
        pass

    def deserialize(self):
        # Deserialization logic to restore state from a storable format
        pass

```

## Testing 🧪
The test_memento.py file should contain tests to verify:

- The integrity of saved and restored states.
- That the Originator’s internal state is not exposed outside the Memento.