import unittest
from fib_iterator import FibonacciList, FibonacciListGetItem


class TestFibIterator(unittest.TestCase):
    """Тесты для итератора FibonacciList."""

    def test_normal(self):
        result = list(FibonacciList(list(range(10))))
        self.assertEqual(result, [0, 1, 2, 3, 5, 8])

    def test_with_duplicates(self):
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        result = list(FibonacciList(lst))
        self.assertEqual(result, [0, 1, 2, 3, 5, 8, 1])

    def test_corner_empty(self):
        result = list(FibonacciList(list(range(0))))
        self.assertEqual(result, [])

    def test_corner_zero(self):
        result = list(FibonacciList(list(range(1))))
        self.assertEqual(result, [0])

    def test_corner_one(self):
        result = list(FibonacciList(list(range(2))))
        self.assertEqual(result, [0, 1])


class TestFibIteratorGetItem(unittest.TestCase):
    """Тесты для итератора FibonacciListGetItem."""

    def test_normal(self):
        result = list(FibonacciListGetItem(list(range(10))))
        self.assertEqual(result, [0, 1, 2, 3, 5, 8])

    def test_index_access(self):
        obj = FibonacciListGetItem(list(range(10)))
        self.assertEqual(obj[0], 0)
        self.assertEqual(obj[4], 5)

    def test_corner_empty(self):
        result = list(FibonacciListGetItem([]))
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()