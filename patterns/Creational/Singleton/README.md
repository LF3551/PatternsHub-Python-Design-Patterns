# Singleton Pattern 🌟

## Overview 📖
The Singleton Pattern ensures that a class has only one instance and provides a global point of access to it. This pattern is particularly useful when exactly one object is needed to coordinate actions across the system.

## Use Case 👥
- Managing a connection to a database 🗃️.
- Configuring properties and settings for an application ⚙️.

## Implementation 🛠️
The `singleton.py` file contains a Python class `Singleton` that demonstrates the implementation. The key feature is that any attempts to instantiate a second object simply return a reference to the existing instance.

## Example Usage 📝
```python
singleton1 = Singleton()
print(singleton1)

singleton2 = Singleton()
print(singleton2)

# Check if both instances are the same
print(singleton1 is singleton2)

```
## Output 📊
```python
Creating the instance
<__main__.Singleton object at 0x10239be60>
<__main__.Singleton object at 0x10239be60>
True
```
This output confirms that only one instance of the Singleton class is created, regardless of how many times it is instantiated. The address in memory is the same for both singleton1 and singleton2, and the comparison returns True, proving that both variables refer to the same instance.

## Business Logic Method 🧠

Here is how you can use the Singleton class to perform some business logic:
```python
singleton = Singleton()
singleton.some_business_logic()
```
## Testing 🧪
The `test_singleton.py` includes tests to ensure that the Singleton pattern is maintained and that multiple instantiations return the same object.
