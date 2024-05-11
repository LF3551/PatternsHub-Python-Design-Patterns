# Chain of Responsibility Pattern 🔗

## Overview 📖
The Chain of Responsibility Pattern allows passing requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain. This pattern decouples the sender of a request from its receivers by giving multiple objects a chance to handle the request.

## Use Cases 🔍
- **Event Bubbling in UI Frameworks**: Where an event can be handled at different stages of the hierarchy.
- **Approval Processes**: Requests pass through a chain of authorities until one of them approves the request.
- **Flexible Error Handling**: Errors can be handled at multiple levels depending on the handler's capability.

## Implementation 🛠️
The `chain_of_responsibility.py` file generally includes:
- An abstract `Handler` class with a method to set the next handler and to handle requests.
- Concrete `Handler` subclasses that implement their specific handling logic.

## Example Usage 📝
```python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            self._successor.handle(request)

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request > 0 and request <= 10:
            print(f"Handler1 handles request {request}")
        else:
            super().handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request > 10 and request <= 20:
            print(f"Handler2 handles request {request}")
        else:
            super().handle(request)

class DefaultHandler(Handler):
    def handle(self, request):
        print(f"DefaultHandler handles request {request}")

# Setting up the chain
handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2(handler1)
default_handler = DefaultHandler(handler2)

# Passing different requests
default_handler.handle(5)
default_handler.handle(15)
default_handler.handle(25)
```

## Output 📊

```python
Handler1 handles request 5
Handler2 handles request 15
DefaultHandler handles request 25
```
This output demonstrates how each request is handled by different handlers depending on the request value.

## Business Logic Method 🧠

The Chain of Responsibility can be tailored to complex decision-making processes where a request may need to pass through multiple checks or operations:

```python
class SecurityCheck(Handler):
    def handle(self, request):
        if "secure" in request:
            print("Security Check Passed.")
            super().handle(request)
        else:
            print("Security Check Failed. Request denied.")

# Example usage
security = SecurityCheck(default_handler)
security.handle({"secure": True, "data": "some sensitive data"})
security.handle({"data": "some sensitive data"})
```
## Testing 🧪

The test_chain_of_responsibility.py file should contain tests that:

Ensure each handler processes appropriate requests as expected.
Confirm requests fall through to the correct handler when one handler cannot deal with them.
Verify the entire chain handles integration scenarios correctly.