# Proxy Pattern 🛡️

## Overview 📖
The Proxy Pattern provides a surrogate or placeholder object that controls access to a more complex or resource-intensive object. This can be useful for managing access to sensitive or expensive resources.

## Use Cases 🔍
- **Lazy Initialization**: Delay the creation of an object until it is actually needed to reduce system load and resource costs.
- **Access Control**: Restrict access to sensitive objects by checking permissions before performing actions.
- **Logging**: Automatically log all operations performed on an object to monitor and audit behavior.


## Implementation 🛠️
The `proxy.py` file contains:
- The `Subject` interface, which is shared by both the RealSubject and the Proxy.
- The `RealSubject` class, which contains the core business logic.
- The `Proxy` class, which controls access to the RealSubject.

## Example Usage 📝
```python
real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()
```
## Output 📊
```python
Proxy: Checking access prior to firing a real request.
RealSubject: Handling request.
Proxy: Logging the time of request.
```
This output illustrates the Proxy's role in managing operations on the RealSubject, demonstrating the added layers of control and accountability.

## Business Logic Method 🧠

The Proxy Pattern can be expanded to incorporate more complex security mechanisms, such as role-based access control or resource usage monitoring. For example, a Virtual Proxy can be used for lazy initialization to optimize resource allocation:

```python
class VirtualProxy(Subject):
    def __init__(self):
        self._real_subject = None

    def request(self):
        if not self._real_subject:
            self._real_subject = RealSubject()
        self._real_subject.request()

# Example usage
if __name__ == "__main__":
    virtual_proxy = VirtualProxy()
    virtual_proxy.request()
```

## Testing 🧪
The `test_proxy.py` file contains tests designed to verify that the Proxy correctly handles:
- Access Control: Ensuring that requests are only processed after successful permission checks.
- Lazy Initialization: Confirming that the RealSubject is only created when required, thereby optimizing resource use.