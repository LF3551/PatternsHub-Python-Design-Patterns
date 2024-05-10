# Prototype Pattern 🛠️

## Overview 📖
The Prototype Pattern is used to create duplicate objects while keeping performance in mind. It helps in creating objects more conveniently.

## Use Cases 🔍
- When the classes to instantiate are specified at runtime.
- For avoiding the overhead of creating objects in a standard way (e.g., using `new`), especially when it is complex or time-consuming.

## Implementation 🛠️
The `prototype.py` file contains a Prototype base class and a ConcretePrototype class that clones itself.

## Example Usage 📝
```python
prototype_original = ConcretePrototype1(1001)
prototype_clone = prototype_original.clone()
print("Original:", prototype_original)
print("Clone:", prototype_clone)
```
## Output 📊
```python
Original: Prototype Number: 1001
Clone: Prototype Number: 1001
```
This example demonstrates the cloning of a prototype object with its internal state.

## Business Logic Method 🧠

Extend the prototype pattern to include complex scenarios where prototypes might need to have deep copy functionality, which involves copying of objects containing other objects.

## Testing 🧪
The `test_prototype.py` file includes tests to ensure that the Prototype pattern is correctly implemented, verifying that the cloned objects maintain the same state as the original without being the same instance.
