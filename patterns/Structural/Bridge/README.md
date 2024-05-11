# [Bridge Pattern](../) 🌉

## Overview 📖
The Bridge Pattern is designed to separate a class's interface from its implementation, allowing the two to vary independently. This pattern is particularly useful for coping with platform dependencies or when adding functionality while minimizing code dependencies.

## Use Cases 🔍
- When you want to avoid a permanent binding between an abstraction and its implementation. This might be the case when the implementation must be selected or switched at runtime.
- When both the abstractions and their implementations should be extendable through subclassing.

## Implementation 🛠️
The `bridge.py` file contains the implementation of the Bridge pattern, including the `Implementor` interface, its concrete implementations, and an `Abstraction` class that uses an `Implementor`.

## Example Usage 📝
```python
implementation_a = ConcreteImplementorA()
abstraction = RefinedAbstraction(implementation_a)
print(abstraction.operation())

implementation_b = ConcreteImplementorB()
abstraction.implementor = implementation_b
print(abstraction.operation())
```
## Output 📊
```python
RefinedAbstraction: Extended operation with:
ConcreteImplementorA: Here's the result on platform A.
RefinedAbstraction: Extended operation with:
ConcreteImplementorB: Here's the result on platform B.
```
This example demonstrates the flexibility of changing the implementation in the abstraction layer without altering its clients.

## Business Logic Method 🧠

The Bridge pattern can be extended to handle more complex scenarios by integrating additional logic within the abstraction hierarchy. For example, you can create abstractions that represent different types of high-level operations, while the implementations can be focused on detailed, platform-specific operations.

Here's how you could incorporate more complex business logic:

```python
class AdvancedAbstraction(RefinedAbstraction):
    """An extension of the RefinedAbstraction that incorporates more complex business logic."""
    def complex_operation(self):
        result = self.implementor.operation_implementation()
        return f"AdvancedAbstraction: Complex processing of {result}"
    
    def multi_step_operation(self):
        step_one = self.implementor.operation_implementation()
        step_two = f"Processed {step_one}"
        return f"AdvancedAbstraction: Multi-step operation with final result: {step_two}"
```
This extension allows the AdvancedAbstraction to perform more sophisticated operations using the basic operations provided by the implementor. It showcases the flexibility of the Bridge pattern in separating concerns, allowing the abstract part to focus on higher-level logic while the implementor takes care of the low-level details.

## Testing 🧪
The `test_bridge.py` file includes tests to verify the separation of abstraction from implementation, ensuring that they can vary independently without impacting each other.