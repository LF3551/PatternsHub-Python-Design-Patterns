# [Behavioral Design Patterns](../../) 🧠

Behavioral design patterns are concerned with improving communication between disjointed objects in a system. They help to define clear and efficient interaction patterns between objects, enhancing the flexibility in carrying out communication. These patterns are essential for creating robust and scalable system architectures. 🎯

## Patterns Covered 📚

### 1. Observer 📡
The Observer pattern allows an object, known as the subject, to notify other objects, known as observers, about changes in its state. The observer objects can then take appropriate action in response to these changes.

Usage: Extremely useful in scenarios where an action taken on one object needs to result in a modification in other objects, such as GUI implementations or data monitoring systems. 🔄

### 2. Strategy 🛡️
The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

Usage: Particularly valuable when you have multiple algorithms for a specific task and want to switch between them dynamically depending on the situation. 🛠️

### 3. Command 📋
The Command pattern turns a request into a stand-alone object that contains all information about the request. This transformation allows you to parameterize methods with different requests, delay or queue a request's execution, and support undoable operations.

Usage: Ideal for operations where actions need to be triggered as objects, allowing for features like command queuing and undo functionality. 👥

### 4. State 🔄
The State pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

Usage: Useful for objects that need to adjust their behavior when their internal state changes, without scattering conditionals and state management throughout the code. 📐

### 5. Template Method 📐
The Template Method pattern defines the skeleton of an algorithm in an operation, deferring some steps to client subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

Usage: Effective when multiple steps of a process are fixed, and only a few steps are changing, providing a framework that offers flexibility while maintaining consistency. 🔁

### 6. Chain of Responsibility 🛡️
The Chain of Responsibility pattern allows a request to be passed along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain.

Usage: Useful in scenarios where multiple objects may handle a request, but the handler isn't known in advance. 🔄

### 7. Iterator 🔍
The Iterator pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

Usage: Particularly valuable for collections to provide a standard way to traverse through the items without exposing the underlying complexity. 👥

### 8. Mediator 🕊️
The Mediator pattern reduces coupling between classes by providing a central authority through which different components may communicate indirectly.

Usage: Effective in reducing direct communications between related objects, making it easier to modify and manage interactions. 📐

### 9. Memento 📝
The Memento pattern captures and externalizes an object's internal state so that the object can be restored to this state later.

Usage: Useful when a snapshot of an object's state must be saved so that it can be restored to that state later. 🔁

### 10. Visitor ✈️
The Visitor pattern lets you define a new operation without changing the classes of the elements on which it operates.

Usage: Highly useful when you need to perform operations across a diverse set of objects without changing their classes. 👥


## Implementation 🔧

Each pattern is implemented in its own subdirectory within this repository:
- Observer
- Strategy
- Command
- State
- TemplateMethod
- Chain of Responsibility
- Iterator
- Mediator
- Memento
- Visitor

Each directory contains:
- Implementation scripts.
- A README.md explaining the pattern and providing examples.
- Tests validating the implementation of the patterns.

## Testing 🧪

You can run the test suite included in each pattern's subdirectory to ensure that the implementations follow the pattern correctly and meet the expected output.