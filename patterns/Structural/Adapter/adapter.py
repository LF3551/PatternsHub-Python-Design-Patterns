class Target:
    """The Target defines the domain-specific interface used by the client code."""
    def request(self):
        return "Target: The default target's behavior."

class Adaptee:
    """The Adaptee contains some useful behavior, but its interface is incompatible with the existing client code.
    The Adaptee needs some adaptation before the client code can use it."""
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laiceps"

class Adapter(Target, Adaptee):
    """The Adapter makes the Adaptee's interface compatible with the Target's interface via multiple inheritance."""
    def request(self):
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"

# Example usage
if __name__ == "__main__":
    target = Target()
    print("Client: I can work just fine with the Target objects:")
    print(target.request())

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    print(adaptee.specific_request())

    adapter = Adapter()
    print("Client: But I can work with it via the Adapter:")
    print(adapter.request())
