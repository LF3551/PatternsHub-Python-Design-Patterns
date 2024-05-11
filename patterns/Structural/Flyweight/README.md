# [Flyweight Pattern](../) 🪶

## Overview 📖
The Flyweight Pattern conserves memory by sharing large numbers of fine-grained objects efficiently. It is typically used to reduce the memory footprint of applications with large numbers of similar objects.

## Use Cases 🔍
- When an application uses a large number of objects that have similar states.
- To reduce the RAM footprint of a heavily object-loaded application.

## Implementation 🛠️
The `flyweight.py` file contains:
- The `Flyweight` class, which stores the intrinsic state shared across several objects.
- The `FlyweightFactory` class, which manages flyweight instances and ensures they are shared properly, thus preventing the creation of redundant objects.


## Example Usage 📝
```python
# Initializing a flyweight factory with two car models
factory = FlyweightFactory([["Chevrolet", "Camaro2018", "pink"], ["Mercedes Benz", "C300", "black"]])

# Retrieving a flyweight and passing extrinsic state for operation
flyweight = factory.get_flyweight(["Chevrolet", "Camaro2018", "pink"])
flyweight.operation(["CL234IR"])
```
## Output 📊
```python
FlyweightFactory: I have 2 flyweights:
Chevrolet_Camaro2018_pink
Mercedes_Benz_C300_black
Flyweight: Displaying shared (Chevrolet, Camaro2018, pink) and unique (CL234IR) state.
```
This demonstrates how the flyweight is shared and displays both its intrinsic and extrinsic state.

## Business Logic Method 🧠

The Flyweight pattern can be adapted to manage shared resources in more complex scenarios, such as networked devices or pooled database connections. Here’s how Flyweights could manage database connections more efficiently:

```python
class ConnectionFlyweight(Flyweight):
    def operation(self, query):
        # Using shared connection details to execute a database query
        print(f"Executing '{query}' on {self._shared_state['server']} using credentials {self._shared_state['credentials']}.")

# Example usage
if __name__ == "__main__":
    db_factory = FlyweightFactory([{"server": "Server1", "credentials": "User1:Pass1"}])
    connection = db_factory.get_flyweight({"server": "Server1", "credentials": "User1:Pass1"})
    connection.operation("SELECT * FROM users")
```

## Testing 🧪
The `test_flyweight.py` file includes tests to verify that the Flyweight Factory properly reuses flyweight objects, demonstrating the memory efficiency of the pattern. Tests ensure that identical intrinsic state requests result in the use of existing flyweight instances rather than the creation of new ones, validating the pattern's effectiveness in memory management.