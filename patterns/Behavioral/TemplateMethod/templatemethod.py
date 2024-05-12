import logging

class AbstractClass:
    def template_method(self):
        self.base_operation()
        self.required_operations()
        self.hook()

    def base_operation(self):
        logging.info("AbstractClass says: I am doing the bulk of the work.")

    def required_operations(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def hook(self):
        pass  # Hook is optional and can be overridden by subclasses

class ConcreteClassA(AbstractClass):
    def required_operations(self):
        logging.info("ConcreteClassA says: Implemented Operation1")

class ConcreteClassB(AbstractClass):
    def required_operations(self):
        logging.info("ConcreteClassB says: Implemented Operation2")

    def hook(self):
        logging.info("ConcreteClassB says: Overridden Hook")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    concrete_a = ConcreteClassA()
    concrete_a.template_method()

    concrete_b = ConcreteClassB()
    concrete_b.template_method()
