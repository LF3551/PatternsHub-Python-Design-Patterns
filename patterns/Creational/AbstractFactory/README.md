# [Abstract Factory Patter](../) 🏭

## Overview 🌐
The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. This pattern is particularly useful for systems configured with one of multiple families of products.

## Use Cases 🔍
- A system should be configured with one of multiple families of products 🏢.
- A family of related product objects is designed to be used together, which requires enforcing this constraint 👨‍👩‍👧‍👦.
- Providing a class library of products where only their interfaces are revealed, not the implementations 📚.

## Implementation 🛠️
The `abstract_factory.py` file contains the implementation that defines abstract and concrete factories. These factories produce a set of related products without specifying their concrete classes. Abstract products declare interfaces for a set of distinct but related products that make up a product family, and concrete products are produced by corresponding concrete factories.

## Example Usage 📝
```python
# Create a concrete factory
factory = ConcreteFactory1()
# Create products using the factory
product_a = factory.create_product_a()
product_b = factory.create_product_b()

# Use the products
print(product_a.use())
print(product_b.use())
```

## Output 📊
```python
ProductA1 used with ProductB1
ProductB1 interacts with ProductA1
```
This output demonstrates how products created by an abstract factory interact, showing the dynamic creation and interaction of objects within a family.

## Business Logic Method 🧠
Here is how you can use the Singleton class to perform some business logic:
```python
# Initialize a factory
factory = ConcreteFactory2()
# Create products
product_a = factory.create_product_a()
product_b = factory.create_product_b()

# Business logic that utilizes created products
print(product_a.operate())
print(product_b.operate())
```
## Testing 🧪
The `test_abstract_factory.py` file includes tests to ensure that different product types are created by different factories correctly, and that each product type corresponds correctly to its factory. These tests help verify the integrity and correct implementation of the Abstract Factory pattern.
