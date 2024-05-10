class Implementor:
    """Implementor class: Defines the interface for implementation classes."""
    def operation_implementation(self):
        pass

class ConcreteImplementorA(Implementor):
    """ConcreteImplementorA: Implements the Implementor interface."""
    def operation_implementation(self):
        return "ConcreteImplementorA: Here's the result on platform A."

class ConcreteImplementorB(Implementor):
    """ConcreteImplementorB: Implements the Implementor interface."""
    def operation_implementation(self):
        return "ConcreteImplementorB: Here's the result on platform B."

class Abstraction:
    """Abstraction class: Defines the abstraction's interface."""
    def __init__(self, implementor):
        self.implementor = implementor

    def operation(self):
        return f"Abstraction: Base operation with:\n{self.implementor.operation_implementation()}"

class RefinedAbstraction(Abstraction):
    """RefinedAbstraction: Extends the interface defined by Abstraction."""
    def operation(self):
        return f"RefinedAbstraction: Extended operation with:\n{self.implementor.operation_implementation()}"

# Example usage
if __name__ == "__main__":
    implementation_a = ConcreteImplementorA()
    abstraction = RefinedAbstraction(implementation_a)
    print(abstraction.operation())

    implementation_b = ConcreteImplementorB()
    abstraction.implementor = implementation_b
    print(abstraction.operation())
