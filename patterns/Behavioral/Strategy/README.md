# [Strategy Pattern](../) 🧠

## Overview 📖
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it. This pattern is typically used to select the appropriate algorithm at runtime according to the need.

## Use Cases 🔍
- **Contextual Algorithms**: Use different algorithms or policies in different contexts, efficiently switching between them at runtime.
- **Performance Optimization**: Change algorithms dynamically to optimize performance based on runtime data.
- **Algorithm Isolation**: Decouple the implementation of an algorithm from the code that uses it, making it easier to switch or modify algorithms without affecting the client.

## Implementation 🛠️
The `strategy.py` file contains:
- A `Context` class to maintain a reference to one of the concrete strategies and can define an interface to let the strategy access its data.
- An `IStrategy` interface for all supported algorithms.
- Concrete `Strategy` classes implementing the `IStrategy` interface.

## Example Usage 📝
```python
class IStrategy:
    def execute(self, data):
        pass

class ConcreteStrategyA(IStrategy):
    def execute(self, data):
        print(f"Processing data with strategy A: {data}")

class ConcreteStrategyB(IStrategy):
    def execute(self, data):
        print(f"Processing data with strategy B: {data}")

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def do_something(self, data):
        self._strategy.execute(data)

## Example usage
context = Context(ConcreteStrategyA())
context.do_something("Test data")
context.set_strategy(ConcreteStrategyB())
context.do_something("Test data")
```

## Output 📊
```python
Processing data with strategy A: Test data
Processing data with strategy B: Test data
```
This output illustrates how the context seamlessly transitions between different strategies.

## Business Logic Method 🧠
The Strategy Pattern can also be used to handle complex decision-making processes where different strategies can be swapped depending on the situation at hand.
```python
class AdvancedStrategy(IStrategy):
    def execute(self, data):
        # Complex decision-making logic here
        print(f"Advanced processing of {data}")

# Adding new strategy to the context
advanced_strategy = AdvancedStrategy()
context.set_strategy(advanced_strategy)
context.do_something("Complex data")
```
## Testing 🧪
The test_strategy.py file should contain tests verifying:
- Correct execution of each strategy.
- Proper switching between strategies.
- Isolation of strategy execution from the context.