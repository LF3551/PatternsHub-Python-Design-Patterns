class Component:
    """Component class declares the interface for objects in the composition."""
    def operation(self):
        pass

class Leaf(Component):
    """Leaf represents end objects in a composition. A leaf has no children."""
    def operation(self):
        return "Leaf"

class Composite(Component):
    """Composite stores child components and implements child-related operations in the component interface."""
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Branch({', '.join(results)})"

# Example usage
if __name__ == "__main__":
    leaf1 = Leaf()
    leaf2 = Leaf()
    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)
    print(composite.operation())
