import logging

class Strategy:
    def execute(self):
        raise NotImplementedError("Subclass must implement abstract method")

class ConcreteStrategyA(Strategy):
    def execute(self):
        logging.info("Executing strategy A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        logging.info("Executing strategy B")

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_some_logic(self):
        logging.info("Context is executing strategy.")
        self.strategy.execute()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    context = Context(ConcreteStrategyA())
    context.do_some_logic()  # This will execute ConcreteStrategyA
    context.set_strategy(ConcreteStrategyB())
    context.do_some_logic()  # This will execute ConcreteStrategyB
