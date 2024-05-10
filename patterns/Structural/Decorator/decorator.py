class Component:
    """Defines the interface for objects that can have responsibilities added to them dynamically."""
    def operation(self):
        pass

class ConcreteComponent(Component):
    """Defines an object to which additional responsibilities can be attached."""
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    """Decorator class 'wraps' a component by maintaining a reference to it and defining an interface that conforms to Component's."""
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    """Adds responsibilities to the component."""
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    """Adds more responsibilities to the component."""
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

# Example usage
if __name__ == "__main__":
    simple = ConcreteComponent()
    decorated = ConcreteDecoratorA(simple)
    more_decorated = ConcreteDecoratorB(decorated)
    print(more_decorated.operation())
