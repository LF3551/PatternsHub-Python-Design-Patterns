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

class Aggregate:
    def __init__(self, collection):
        self._collection = collection

    def create_iterator(self):
        return Iterator(self._collection)

if __name__ == "__main__":
    agg = Aggregate(['a', 'b', 'c', 'd'])
    iterator = agg.create_iterator()
    while iterator.has_next():
        print(iterator.next())
