from abc import ABC, abstractmethod

class Subject(ABC):
    """Subject declares common operations for both RealSubject and Proxy."""
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    """RealSubject contains the core business logic."""
    def request(self):
        print("RealSubject: Handling request.")

class Proxy(Subject):
    """Proxy controls access to the RealSubject, allowing additional functionality."""
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()
        else:
            print("Proxy: Access denied.")

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        # Simplified access check
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

# Example usage
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()
