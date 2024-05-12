import logging

class State:
    def handle(self, context):
        raise NotImplementedError("Subclass must implement abstract method")

class ConcreteStateA(State):
    def handle(self, context):
        logging.info("ConcreteStateA is handling the context.")
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        logging.info("ConcreteStateB is handling the context.")
        context.state = ConcreteStateA()

class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    context = Context(ConcreteStateA())
    context.request()  # This will switch to ConcreteStateB
    context.request()  # This will switch back to ConcreteStateA
