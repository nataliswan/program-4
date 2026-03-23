from typing import List, Iterable, Iterator, Set


def _generate_fib_set(max_val: int) -> Set[int]:
    """
    Сгенерировать множество чисел Фибоначчи до max_val.

    Аргументы:
        max_val: Максимальное значение для поиска чисел Фибоначчи.

    Возвращает:
        Множество чисел Фибоначчи.
    """
    if max_val < 0:
        return set()

    fibs = {0, 1}
    a, b = 0, 1
    while b <= max_val:
        a, b = b, a + b
        fibs.add(a)
    return fibs


class FibonacciList:
    """
    Итератор для фильтрации чисел Фибоначчи из списка.
    Реализация через протокол итератора (__iter__, __next__).
    """

    def __init__(self, instance: Iterable[int]) -> None:
        """
        Инициализировать итератор.

        Аргументы:
            instance: Входной список чисел.
        """
        self.instance = list(instance)
        self.idx = 0
        if self.instance:
            self.fib_set = _generate_fib_set(max(self.instance))
        else:
            self.fib_set = set()

    def __iter__(self) -> Iterator[int]:
        """Вернуть сам объект итератора."""
        return self

    def __next__(self) -> int:
        """
        Вернуть следующий элемент списка, являющийся числом Фибоначчи.

        Возвращает:
            Следующее число Фибоначчи.

        Исключения:
            StopIteration: Если элементы закончились.
        """
        while True:
            if self.idx >= len(self.instance):
                raise StopIteration

            value = self.instance[self.idx]
            self.idx += 1

            if value in self.fib_set:
                return value


class FibonacciListGetItem:
    """
    Итератор через протокол последовательности (__getitem__).
    Позволяет обращаться к объекту как к списку.
    """

    def __init__(self, instance: Iterable[int]) -> None:
        """
        Инициализировать объект.

        Аргументы:
            instance: Входной список чисел.
        """
        self.instance = list(instance)
        if self.instance:
            self.fib_set = _generate_fib_set(max(self.instance))
        else:
            self.fib_set = set()

        self._filtered_data = [x for x in self.instance if x in self.fib_set]

    def __getitem__(self, index: int) -> int:
        """
        Вернуть элемент по индексу.

        Аргументы:
            index: Индекс элемента.

        Возвращает:
            Число Фибоначчи.

        Исключения:
            IndexError: Если индекс выходит за границы.
        """
        return self._filtered_data[index]

    def __iter__(self) -> Iterator[int]:
        """Сделать объект итерируемым через __getitem__."""
        return iter(self._filtered_data)