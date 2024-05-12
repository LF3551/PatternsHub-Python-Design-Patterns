import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Iterator.iterator import Aggregate, Iterator

class TestIteratorPattern(unittest.TestCase):
    def test_iterator(self):
        collection = ['a', 'b', 'c', 'd']
        agg = Aggregate(collection)
        iterator = agg.create_iterator()
        
        result = []
        while iterator.has_next():
            result.append(iterator.next())

        self.assertEqual(result, ['a', 'b', 'c', 'd'])
        with self.assertRaises(StopIteration):
            iterator.next()

if __name__ == '__main__':
    unittest.main()
