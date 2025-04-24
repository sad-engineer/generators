#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
"""Модуль с числовыми генераторами."""

import random
from typing import Generator


def positive_numbers() -> Generator[int, None, None]:
    """Генератор положительных чисел."""
    num = 1
    while True:
        yield num
        num += 1


def prime_numbers() -> Generator[int, None, None]:
    """Генератор простых чисел."""
    def is_prime(n: int) -> bool:
        """Проверяет, является ли число простым."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def even_numbers() -> Generator[int, None, None]:
    """Генератор четных чисел (2, 4, 6, ...)."""
    num = 2
    while True:
        yield num
        num += 2


def odd_numbers() -> Generator[int, None, None]:
    """Генератор нечетных чисел (1, 3, 5, ...)."""
    num = 1
    while True:
        yield num
        num += 2


def square_numbers() -> Generator[int, None, None]:
    """Генератор квадратов чисел (1, 4, 9, 16, ...)."""
    num = 1
    while True:
        yield num ** 2
        num += 1


def cube_numbers() -> Generator[int, None, None]:
    """Генератор кубов чисел (1, 8, 27, 64, ...)."""
    num = 1
    while True:
        yield num ** 3
        num += 1


def fibonacci() -> Generator[int, None, None]:
    """Генератор чисел Фибоначчи (0, 1, 1, 2, 3, 5, ...)."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def factorial() -> Generator[int, None, None]:
    """Генератор факториалов (1, 2, 6, 24, 120, ...)."""
    num, fact = 1, 1
    while True:
        yield fact
        num += 1
        fact *= num


def powers_of_two() -> Generator[int, None, None]:
    """Генератор степеней двойки (1, 2, 4, 8, 16, ...)."""
    num = 1
    while True:
        yield num
        num *= 2


def random_numbers() -> Generator[int, None, None]:
    """Генератор случайных чисел от 1 до 100."""
    while True:
        yield random.randint(1, 100)


def formatted_decimal_strings(digits: int) -> Generator[str, None, None]:
    """
    Универсальный генератор форматированных строк.

    :param digits: Количество знаков после точки (например, 2 → .01, 3 → .001).
    """
    for num in positive_numbers():
        num -= 1
        yield f".{num:0{digits}d}"
