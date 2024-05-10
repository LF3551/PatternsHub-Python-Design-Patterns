class Flyweight:
    """The Flyweight stores a common portion of the state (also called intrinsic state)
    that belongs to multiple real business entities. The Flyweight accepts the rest of the
    state (extrinsic state, unique for each entity) via its method parameters."""
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        s = str(self._shared_state)
        u = str(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.")

class FlyweightFactory:
    """The Flyweight Factory creates and manages the Flyweight objects. It ensures
    that flyweights are shared correctly. When the client requests a flyweight,
    the factory either returns an existing instance or creates a new one, if it
    doesn't exist yet."""
    _flyweights = {}

    def __init__(self, initial_flyweights):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state):
        """Returns a Flyweight's string hash for a given state."""
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state):
        """Returns an existing Flyweight with a given state or creates a new one."""
        key = self.get_key(shared_state)
        if not key in self._flyweights:
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")
        return self._flyweights[key]

    def list_flyweights(self):
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())))

# Example usage
if __name__ == "__main__":
    factory = FlyweightFactory([["Chevrolet", "Camaro2018", "pink"], ["Mercedes Benz", "C300", "black"]])
    factory.list_flyweights()
    add_car = factory.get_flyweight(["Chevrolet", "Camaro2018", "pink"])
    add_car.operation(["CL234IR"])
