# [Facade Pattern](../) 🏢

## Overview 📖
The Facade Pattern provides a simplified interface to a complex subsystem, making it easier for client applications to interact with the system. It helps to decouple the system from clients and other subsystems, promoting subsystem independence and portability.

## Use Cases 🔍
- When you want to provide a simple interface to a complex subsystem.
- When there are many dependencies between clients and the implementation classes of an abstraction.

## Implementation 🛠️
The `facade.py` file contains the Facade class that encapsulates the complexity of the subsystems (Subsystem1 and Subsystem2) and provides a simple interface to the clients.

## Example Usage 📝
```python
subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
facade = Facade(subsystem1, subsystem2)
print(facade.operation())
```
## Output 📊
```python
Facade initializes subsystems:
Subsystem1: Ready!
Subsystem2: Get ready!
Facade orders subsystems to perform the action:
Subsystem1: Go!
Subsystem2: Fire!
```
This example demonstrates how the Facade provides a single, unified, and simplified interface to the more complex subsystems beneath.

## Business Logic Method 🧠
The Facade pattern can be extended to provide more comprehensive management features, such as error handling, logging, or security checks. Here's an example of integrating security checks into the facade to enhance system security:

```python
class SecureFacade(Facade):
    def operation(self):
        if not self.check_security():
            return "Security check failed: Access denied!"
        return super().operation()

    def check_security(self):
        # Here we could implement various security checks.
        return True

# Example usage
if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    secure_facade = SecureFacade(subsystem1, subsystem2)
    print(secure_facade.operation())
```

## Testing 🧪
The `test_facade.py` file includes tests to ensure that the Facade properly delegates client requests to the subsystems and integrates all subsystem operations correctly. Specific tests verify that the facade effectively handles errors and security checks, ensuring robust operation.