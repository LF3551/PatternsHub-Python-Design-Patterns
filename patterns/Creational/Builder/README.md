# [Builder Pattern](../) 🏗️

## Overview 📖
The Builder Pattern separates the construction of a complex object from its representation, allowing the construction process to create different representations.

## Use Cases 🔍
- When the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled.
- When the construction process must allow different representations for the object that's constructed.

## Implementation 🛠️
The `builder.py` file contains the implementation with abstract and concrete builder classes. A Director class is used to construct the object using the Builder interface.

## Example Usage 📝
```python
director = Director(ConcreteBuilder())
director.construct()
product = director.builder.get_result()
print("Product constructed:", product)
```
## Output 📊
```python
Product constructed: ['Part A', 'Part B']
```
This example demonstrates building a product with parts A and B. The Director manages the construction process, and the ConcreteBuilder provides the specifics.

## Business Logic Method 🧠
The Builder pattern can be used to encapsulate the complex construction process of an object that involves various steps and components. Here’s how you can extend the builder pattern to perform complex business logic:
```python
class ComplexProductBuilder(ConcreteBuilder):
    def add_feature_x(self):
        self.product.append("Feature X")

    def add_feature_y(self):
        self.product.append("Feature Y")

# Extend the director to use the new builder
class ExtendedDirector(Director):
    def construct_with_features(self):
        self._builder.create_new_product()
        self._builder.build_part_a()
        self._builder.add_feature_x()
        self._builder.build_part_b()
        self._builder.add_feature_y()

# Example usage
if __name__ == "__main__":
    builder = ComplexProductBuilder()
    director = ExtendedDirector(builder)
    director.construct_with_features()
    product = builder.get_result()
    print("Product with advanced features:", product)
```
## Testing 🧪
The `test_builder.py` file includes tests to ensure the Builder pattern is maintained, validating that the constructed product meets the expected parts configuration.
