import copy

class Prototype:
    """Prototype class: Create a new object by cloning an existing object."""
    def clone(self):
        """Creates a clone of this object."""
        return copy.deepcopy(self)

class ConcretePrototype1(Prototype):
    """Concrete Prototype class: Implements an operation for cloning itself."""
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Prototype Number: {self.number}"

# Example usage
if __name__ == "__main__":
    prototype_original = ConcretePrototype1(1001)
    prototype_clone = prototype_original.clone()
    print(prototype_original)
    print(prototype_clone)
