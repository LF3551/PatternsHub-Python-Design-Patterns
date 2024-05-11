# [Composite Pattern](../) 🌳

## Overview 📖
The Composite Pattern allows you to work with complex tree structures more conveniently, treating simple and composite elements uniformly.

## Use Cases 🔍
- When you need to represent a part-whole hierarchy of objects.
- When you want clients to ignore the difference between compositions of objects and individual objects.

## Implementation 🛠️
The `composite.py` file contains the Component, Leaf, and Composite classes. Composite's `operation` method recursively calls similar operations on child components, combining their results.

## Example Usage 📝
```python
leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
print(composite.operation())
```
## Output 📊
```python
Branch(Leaf, Leaf)
```
This example demonstrates how Composite groups individual Leaf objects and treats them uniformly through the Component interface.

## Business Logic Method 🧠

Extend the Composite pattern to handle more complex data processing by incorporating additional functionality in the Composite's operations. Here's an example of adding data summarization capabilities:

```python
class DataComposite(Composite):
    def summarize_data(self):
        sum_data = sum(child.data for child in self.children if hasattr(child, 'data'))
        return f"Total Sum: {sum_data}"

class DataLeaf(Leaf):
    def __init__(self, data):
        self.data = data

# Example usage
if __name__ == "__main__":
    leaf1 = DataLeaf(10)
    leaf2 = DataLeaf(20)
    composite = DataComposite()
    composite.add(leaf1)
    composite.add(leaf2)
    print(composite.summarize_data())

```

## Testing 🧪
The `test_composite.py` file includes tests to verify that the Composite and Leaf behave correctly, ensuring that compositions and individual elements are treated uniformly.