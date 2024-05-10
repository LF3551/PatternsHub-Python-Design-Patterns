# Factory Method Pattern

## Overview
The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. It lets a class defer instantiation to subclasses, enhancing flexibility and encapsulation.

## Use Case
- Useful when there is a need to manage and maintain a large collection of smaller objects that share properties.
- Often used in applications where management of database connections and their allocation is needed.

## Implementation
The `factory_method.py` file contains a Python class that demonstrates the implementation. This pattern uses a creator class with a default implementation of the factory method that returns a default object, but it also allows subclasses to override this method to return different types of objects.

## Example Usage
```python
creator = ConcreteCreator()
product = creator.factory_method()
print(product.operation())
```

## Output
```python
Result of the ConcreteProduct operation.
```
This output shows how the product created by the factory method performs its operation, demonstrating the dynamic creation of objects.

## Testing
The test_factory_method.py file includes tests to ensure that the Factory Method pattern is correctly implemented and that it can dynamically create various types of product instances.