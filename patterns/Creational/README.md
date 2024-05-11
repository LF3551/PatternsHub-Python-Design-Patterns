# Creational Design Patterns 🛠️

Creational design patterns are concerned with the way of creating objects, allowing objects to be created in a manner suitable to the situation. These patterns reduce complexities and instability by creating objects in a controlled manner. 🎯

## Patterns Covered 📚

### 1. Singleton 🌐
The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.

**Usage**: Useful in scenarios where a single instance of a class should exist across the application, like in configuration settings or database connections. 🔄

### 2. Factory Method 🏭
The Factory Method pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate, thus allowing the instantiation process to be deferred to subclasses.

**Usage**: Particularly useful when there is a need to manage and maintain a collection of related objects without specifying their concrete classes. 🛠️

### 3. Abstract Factory 🎨
The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.

**Usage**: Useful when a system should be independent of how its products are created, composed, and represented. 👥

### 4. Builder 🏗️
The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create various representations.

**Usage**: Useful when there could be several flavors of an object and to avoid constructor telescoping. The key difference from the Factory pattern is that Builder is used when the creation involves several steps. 📐

### 5. Prototype 🐑
The Prototype pattern is used when the types of objects to create are determined by a prototypical instance, which is cloned to produce new objects.

**Usage**: Useful when objects are required that are similar to existing objects, or when the creation would be expensive as compared to cloning. 🔁

## Implementation 🔧
Each pattern is implemented in its own subdirectory within this repository:
- `Singleton`
- `FactoryMethod`
- `AbstractFactory`
- `Builder`
- `Prototype`

Each directory contains:
- Implementation scripts.
- A `README.md` explaining the pattern and providing examples.
- Tests validating the implementation of the patterns.

## Testing 🧪
You can run the test suite included in each pattern's subdirectory to ensure that the implementations follow the pattern correctly and meet the expected output.