# [Decorator Pattern](../) 🎨

## Overview 📖
The Decorator Pattern allows behavior to be added to individual objects, dynamically, without affecting the behavior of other objects from the same class.

## Use Cases 🔍
- When you need to add responsibilities to individual objects dynamically and transparently, without affecting other objects.
- When extending functionality by subclassing is impractical.

## Implementation 🛠️
The `decorator.py` file contains the Component, ConcreteComponent, Decorator, and ConcreteDecorators classes. Decorators wrap a component and incrementally add functionality.

## Example Usage 📝
```python
simple = ConcreteComponent()
decorated = ConcreteDecoratorA(simple)
more_decorated = ConcreteDecoratorB(decorated)
print(more_decorated.operation())
```
## Output 📊
```python
ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
```
This output demonstrates how the decorators dynamically add functionality to the `ConcreteComponent`. Each decorator wraps the previous level, adding its own behavior while preserving the interface.

## Business Logic Method 🧠
The Decorator pattern can be extended to include more complex logic, such as logging, caching, or monitoring of operations, enhancing not just functionality but also the maintainability and scalability of an application. Here's an example of integrating logging functionality:

```python
class LoggingDecorator(Decorator):
    def operation(self):
        result = self._component.operation()
        print(f"Logging: {result}")
        return result

# Example usage
if __name__ == "__main__":
    component = ConcreteComponent()
    logging_decorator = LoggingDecorator(component)
    final_result = logging_decorator.operation()
```

## Testing 🧪
The `test_decorator.py` file includes tests to verify that the Decorator correctly adds new functionalities to the component, maintaining the interface while enhancing behavior. The tests ensure that each decorator adds its intended effect without disrupting the functionality of other decorators or the base component.