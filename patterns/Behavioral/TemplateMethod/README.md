# Template Method Pattern 📐

## Overview 📖
The Template Method Pattern defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure. This pattern is crucial for reusing the invariant parts of an algorithm, while allowing variations in the details.

## Use Cases 🔍
- **Data Processing Algorithms**: Standardize the structure of a data processing algorithm while allowing customization of each step.
- **Workflow Engines**: Define a fixed sequence of steps in a process, allowing different implementations of these steps in various scenarios.
- **Game Development**: Set up a general game structure (like initialization, start play, end play) and let subclasses define specific game mechanics.

## Implementation 🛠️
The `template_method.py` file contains:
- An abstract `AbstractClass` with a template method and abstract methods for steps needing customization.
- Concrete subclasses that implement these abstract methods to complete the specific parts of the algorithm.

## Example Usage 📝
```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.step_one()
        self.step_two()
        self.hook()

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    def hook(self):
        # Optional step, empty default implementation
        pass

class ConcreteClass1(AbstractClass):
    def step_one(self):
        print("ConcreteClass1: Executing Step 1")

    def step_two(self):
        print("ConcreteClass1: Executing Step 2")

class ConcreteClass2(AbstractClass):
    def step_one(self):
        print("ConcreteClass2: Executing Step 1")

    def step_two(self):
        print("ConcreteClass2: Executing Step 2")

    def hook(self):
        print("ConcreteClass2: Custom hook implementation")

# Example usage
concrete1 = ConcreteClass1()
concrete1.template_method()

concrete2 = ConcreteClass2()
concrete2.template_method()
```
# Output 📊

```python
ConcreteClass1: Executing Step 1
ConcreteClass1: Executing Step 2
ConcreteClass2: Executing Step 1
ConcreteClass2: Executing Step 2
ConcreteClass2: Custom hook implementation
```
This output illustrates how ConcreteClass1 and ConcreteClass2 each execute the algorithm's steps, with ConcreteClass2 adding a custom step via the hook method.

# Business Logic Method 🧠

The Template Method can be particularly useful for setting up a comprehensive framework for complex business operations that follow a fixed sequence but need flexibility in some of their phases.

```python
class ReportGenerator(AbstractClass):
    def step_one(self):
        print("Gathering data")

    def step_two(self):
        print("Analyzing data")

    def hook(self):
        print("Generating interactive visualizations")

# Example usage
report = ReportGenerator()
report.template_method()

```
# Testing 🧪

The test_template_method.py file should include tests to verify:

- Each step of the template method is called in the right order.
- Subclass overrides correctly customize the algorithm steps.
- The hook method is optional and does not affect the template method when not overridden.