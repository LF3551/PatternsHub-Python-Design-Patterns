import logging

class Memento:
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state

class Originator:
    _state = ""

    def set(self, state):
        logging.info(f"Originator: Setting state to {state}")
        self._state = state

    def save_to_memento(self):
        logging.info("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()
        logging.info(f"Originator: State after restoring from Memento: {self._state}")

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    originator = Originator()
    caretaker = Caretaker()

    originator.set("State1")
    caretaker.add_memento(originator.save_to_memento())
    originator.set("State2")
    caretaker.add_memento(originator.save_to_memento())

    originator.restore_from_memento(caretaker.get_memento(0))
