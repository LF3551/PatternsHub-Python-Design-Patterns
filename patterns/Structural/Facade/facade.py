class Subsystem1:
    def operation1(self):
        return "Subsystem1: Ready!\n"
    
    def operationN(self):
        return "Subsystem1: Go!\n"

class Subsystem2:
    def operation1(self):
        return "Subsystem2: Get ready!\n"
    
    def operationZ(self):
        return "Subsystem2: Fire!\n"

class Facade:
    """
    The Facade class provides a simple interface to the complex functionality of one or more subsystems.
    It delegates the client requests to appropriate subsystem objects.
    """
    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operationN())
        results.append(self._subsystem2.operationZ())
        return "".join(results)

# Example usage
if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    print(facade.operation())
