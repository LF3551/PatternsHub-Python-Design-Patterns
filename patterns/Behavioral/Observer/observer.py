import logging

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        raise NotImplementedError("Subclass must implement abstract method")

class ConcreteObserverA(Observer):
    def update(self):
        logging.info("ConcreteObserverA: Received an update!")

class ConcreteObserverB(Observer):
    def update(self):
        logging.info("ConcreteObserverB: Received an update!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    subject = Subject()
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()
    subject.attach(observer_a)
    subject.attach(observer_b)
    subject.notify()
