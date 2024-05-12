import logging

class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError("Subclass must implement abstract method")

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            logging.info("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            logging.info("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()

class BaseComponent:
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

class Component1(BaseComponent):
    def do_a(self):
        logging.info("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self):
        logging.info("Component 1 does B.")

class Component2(BaseComponent):
    def do_c(self):
        logging.info("Component 2 does C.")

    def do_d(self):
        logging.info("Component 2 does D.")
        self.mediator.notify(self, "D")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    c1.do_a()
    c2.do_d()
