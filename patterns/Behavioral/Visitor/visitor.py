import logging

class Visitor:
    def visit_element_a(self, element):
        raise NotImplementedError("Subclass must implement abstract method")

    def visit_element_b(self, element):
        raise NotImplementedError("Subclass must implement abstract method")

class Element:
    def accept(self, visitor):
        raise NotImplementedError("Subclass must implement abstract method")

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)
        logging.info("ConcreteElementA is visited.")

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)
        logging.info("ConcreteElementB is visited.")

class ConcreteVisitor1(Visitor):
    def visit_element_a(self, element):
        logging.info("ConcreteVisitor1 is processing ConcreteElementA")

    def visit_element_b(self, element):
        logging.info("ConcreteVisitor1 is processing ConcreteElementB")

class ConcreteVisitor2(Visitor):
    def visit_element_a(self, element):
        logging.info("ConcreteVisitor2 is processing ConcreteElementA")

    def visit_element_b(self, element):
        logging.info("ConcreteVisitor2 is processing ConcreteElementB")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    element_a = ConcreteElementA()
    element_b = ConcreteElementB()
    visitor1 = ConcreteVisitor1()
    visitor2 = ConcreteVisitor2()

    element_a.accept(visitor1)
    element_b.accept(visitor1)
    element_a.accept(visitor2)
    element_b.accept(visitor2)
