class Handler:
    """Abstract Handler"""
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            self._successor.handle(request)
        else:
            raise NotImplementedError("End of chain, no method to handle")

    def set_successor(self, successor):
        self._successor = successor

class ConcreteHandler1(Handler):
    """Concrete Handler #1"""
    def handle(self, request):
        if 0 < request <= 10:
            print(f"Handler 1 is handling request {request}")
        else:
            super().handle(request)

class ConcreteHandler2(Handler):
    """Concrete Handler #2"""
    def handle(self, request):
        if 10 < request <= 20:
            print(f"Handler 2 is handling request {request}")
        else:
            super().handle(request)

class DefaultHandler(Handler):
    """Default Handler"""
    def handle(self, request):
        print(f"Default handler for request {request}")

if __name__ == "__main__":
    h1 = ConcreteHandler1()
    h2 = ConcreteHandler2(DefaultHandler())
    h1.set_successor(h2)  # Correctly setting the successor now

    requests = [2, 14, 22, 5, 17]
    for request in requests:
        h1.handle(request)
