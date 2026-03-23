import functools
from typing import Generator, List, Callable


def fib_elem_gen() -> Generator[int, None, None]:
    """
    Сгенерировать бесконечный ряд чисел Фибоначчи.

    Возвращает:
        Следующее число ряда Фибоначчи (через yield).
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_coroutine(func: Callable[..., Generator[List[int], int, None]]) -> Callable[..., Generator[List[int], int, None]]:
    """
    Активировать корутину автоматически.
    Вызывает gen.send(None) сразу после создания генератора.

    Аргументы:
        func: Функция-генератор.

    Возвращает:
        Обернутая функция.
    """
    @functools.wraps(func)
    def inner(*args: any, **kwargs: any) -> Generator[List[int], int, None]:
        gen = func(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


@fib_coroutine
def my_genn() -> Generator[List[int], int, None]:
    """
    Принять число n и вернуть список чисел Фибоначчи.
    Сопрограмма для двустороннего обмена данными.

    Возвращает:
        Список чисел Фибоначчи (через yield).

    Принимает:
        Количество элементов (int) через send().
    """
    number_of_fib_elem: int = yield []

    while True:
        result: List[int] = []
        a, b = 0, 1
        for _ in range(number_of_fib_elem):
            result.append(a)
            a, b = b, a + b
        number_of_fib_elem = yield result