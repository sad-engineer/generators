#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
"""
Модуль с генераторами различных последовательностей.

Предоставляет функционал для:
- генерации числовых последовательностей
- генерации строковых последовательностей
- генерации последовательностей с историей значений
"""

from generators.container import (
    GeneratorContainer,
    cube_numbers,
    even_numbers,
    factorial,
    fibonacci,
    formatted_decimal_strings,
    odd_numbers,
    positive_numbers,
    powers_of_two,
    prime_numbers,
    random_numbers,
    square_numbers,
    alphabet,
    days_of_week,
    reverse_alphabet,
    reverse_russian_alphabet,
    russian_alphabet,
    GeneratorQueue
)
from generators.interfaces import IGenerator, IGeneratorQueue


__all__ = [
    # Интерфейсы
    'IGenerator',
    'IGeneratorQueue',
    
    # Числовые генераторы
    'positive_numbers',
    'prime_numbers',
    'even_numbers',
    'odd_numbers',
    'square_numbers',
    'cube_numbers',
    'fibonacci',
    'factorial',
    'powers_of_two',
    'random_numbers',
    
    # Строковые генераторы
    'alphabet',
    'reverse_alphabet',
    'russian_alphabet',
    'reverse_russian_alphabet',
    'formatted_decimal_strings',
    'days_of_week',
    
    # Классы
    'GeneratorQueue',
    'GeneratorContainer'
]


if __name__ == "__main__":
    # Пример использования генераторов
    print("Положительные числа:")
    for num in positive_numbers():
        if num > 10: break
        print(num)

    print("\nПростые числа:")
    for num in prime_numbers():
        if num > 30: break
        print(num)

    print("\nЧетные числа:")
    for num in even_numbers():
        if num > 20: break
        print(num)

    print("\nНечетные числа:")
    for num in odd_numbers():
        if num > 20: break
        print(num)

    print("\nКвадраты чисел:")
    for num in square_numbers():
        if num > 100: break
        print(num)

    print("\nАлфавит:")
    for letter in alphabet():
        print(letter)

    print("\nДни недели:")
    for day in days_of_week():
        print(day)
