# [Iterator Pattern](../) 🔄

## Overview 📖
The Iterator Pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. This pattern is essential for encapsulating the traversal of potentially complex data structures and providing a standard interface for iterating over them.

## Use Cases 🔍
- **Collection Traversal**: Allows traversal through various types of collections (like lists, trees, graphs) without needing to expose their internal structures.
- **Data Hiding**: Keeps the internal structure of an aggregate object hidden from the client.
- **Support for Multiple Traversal**: Supports multiple simultaneous traversals of the same aggregate with different iterators.

## Implementation 🛠️
The `iterator.py` file typically includes:
- An `Iterable` interface defining a method for obtaining an iterator.
- An `Iterator` interface defining methods for accessing elements of a collection.
- Concrete `Iterator` and `Iterable` classes implementing these interfaces.

## Example Usage 📝
```python
class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def next(self):
        try:
            value = self._collection[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration()

    def has_next(self):
        return self._index < len(self._collection)

class Iterable:
    def __init__(self, collection):
        self._collection = collection

    def get_iterator(self):
        return Iterator(self._collection)

# Example usage
collection = Iterable([1, 2, 3, 4, 5])
iterator = collection.get_iterator()

while iterator.has_next():
    print(iterator.next())

```
## Output 📊
```python
1
2
3
4
5

```
This output demonstrates the basic functionality of an iterator traversing through a collection of items.

## Business Logic Method 🧠
The Iterator Pattern can also adapt to more complex business scenarios such as iterating over a filtered subset of elements based on certain conditions:
```python
class FilterIterator(Iterator):
    def __init__(self, collection, filter_condition):
        super().__init__(collection)
        self._filter_condition = filter_condition

    def next(self):
        while self.has_next():
            value = super().next()
            if self._filter_condition(value):
                return value
        raise StopIteration()

# Example usage
is_even = lambda x: x % 2 == 0
filtered_iterator = FilterIterator([1, 2, 3, 4, 5], is_even)

while True:
    try:
        print(filtered_iterator.next())
    except StopIteration:
        break

```
## Output 📊
```python
2
4
```

## Testing 🧪
The test_iterator.py file should contain tests verifying:
- Correct traversal of elements.
- Proper handling of the end of the collection.
- Functionality of extended iterators like FilterIterator.