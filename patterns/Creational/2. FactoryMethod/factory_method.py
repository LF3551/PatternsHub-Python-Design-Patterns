class Creator:
    """Declare the factory method, which returns an object of type Product."""
    def factory_method(self):
        return Product()

    def operation(self):
        """Call the factory method to create a Product object."""
        product = self.factory_method()
        return product.operation() 

class Product:
    """An interface for the products created by the factory method."""
    def operation(self):
        return "Result of the Product operation."

class ConcreteProduct(Product):
    """Concrete Products implement the Product interface."""
    def operation(self):
        return "Result of the ConcreteProduct operation."

class ConcreteCreator(Creator):
    """Override the factory method to return an instance of ConcreteProduct."""
    def factory_method(self):
        return ConcreteProduct()

# Example usage
if __name__ == "__main__":
    creator = ConcreteCreator()
    print(creator.operation())