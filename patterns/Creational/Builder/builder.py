class Director:
    """Director class: Constructs an object using the Builder interface."""
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.create_new_product()
        self._builder.build_part_a()
        self._builder.build_part_b()

class Builder:
    """Abstract Builder class: Provides the steps to build the product."""
    def create_new_product(self):
        raise NotImplementedError

    def build_part_a(self):
        raise NotImplementedError

    def build_part_b(self):
        raise NotImplementedError

    def get_result(self):
        raise NotImplementedError

class ConcreteBuilder(Builder):
    """Concrete Builder class: Provides methods to build parts of the product."""
    def __init__(self):
        self.product = []

    def create_new_product(self):
        self.product = []

    def build_part_a(self):
        self.product.append("Part A")

    def build_part_b(self):
        self.product.append("Part B")

    def get_result(self):
        return self.product

# Example usage
if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct()
    product = builder.get_result()
    print("Product parts:", product)
