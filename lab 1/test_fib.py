import unittest
from fib_coroutine import my_genn


class TestFibCoroutine(unittest.TestCase):
    """Тесты для сопрограммы my_genn."""

    def test_fib_3(self):
        gen = my_genn()
        assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3"

    def test_fib_5(self):
        gen = my_genn()
        assert gen.send(5) == [0, 1, 1, 2, 3], "Пять первых членов ряда"

    def test_corner_zero(self):
        gen = my_genn()
        self.assertEqual(gen.send(0), [])

    def test_corner_one(self):
        gen = my_genn()
        self.assertEqual(gen.send(1), [0])

    def test_corner_two(self):
        gen = my_genn()
        self.assertEqual(gen.send(2), [0, 1])

    def test_sequential_calls(self):
        gen = my_genn()
        self.assertEqual(gen.send(3), [0, 1, 1])
        self.assertEqual(gen.send(5), [0, 1, 1, 2, 3])
        self.assertEqual(gen.send(2), [0, 1])


if __name__ == '__main__':
    unittest.main()