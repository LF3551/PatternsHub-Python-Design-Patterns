class AbstractFactory:
    def create_product_a(self):
        raise NotImplementedError

    def create_product_b(self):
        raise NotImplementedError

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()

class AbstractProductA:
    def interact(self, abstract_product_b):
        pass

class ProductA1(AbstractProductA):
    def interact(self, abstract_product_b):
        print(f"ProductA1 interacts with {abstract_product_b}")

class ProductA2(AbstractProductA):
    def interact(self, abstract_product_b):
        print(f"ProductA2 interacts with {abstract_product_b}")

class AbstractProductB:
    def interact(self, abstract_product_a):
        pass

class ProductB1(AbstractProductB):
    def interact(self, abstract_product_a):
        print(f"ProductB1 interacts with {abstract_product_a}")

class ProductB2(AbstractProductB):
    def interact(self, abstract_product_a):
        print(f"ProductB2 interacts with {abstract_product_a}")

# Example usage
if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    product_a1 = factory1.create_product_a()
    product_b1 = factory1.create_product_b()
    product_a1.interact(product_b1)

    factory2 = ConcreteFactory2()
    product_a2 = factory2.create_product_a()
    product_b2 = factory2.create_product_b()
    product_a2.interact(product_b2)