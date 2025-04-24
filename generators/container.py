#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
"""Модуль с контейнером генераторов."""

from dependency_injector import containers, providers

from generators.numeric_generators import (
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
)
from generators.string_generators import (
    alphabet,
    days_of_week,
    reverse_alphabet,
    reverse_russian_alphabet,
    russian_alphabet,
)
from generators.generator_queue import GeneratorQueue


class GeneratorContainer(containers.DeclarativeContainer):
    """
    Контейнер для управления различными генераторами.
    """

    # Числовые генераторы
    positive_numbers_provider = providers.Factory(GeneratorQueue, generator_func=positive_numbers)
    prime_numbers_provider = providers.Factory(GeneratorQueue, generator_func=prime_numbers)
    even_numbers_provider = providers.Factory(GeneratorQueue, generator_func=even_numbers)
    odd_numbers_provider = providers.Factory(GeneratorQueue, generator_func=odd_numbers)
    square_numbers_provider = providers.Factory(GeneratorQueue, generator_func=square_numbers)
    cube_numbers_provider = providers.Factory(GeneratorQueue, generator_func=cube_numbers)
    fibonacci_provider = providers.Factory(GeneratorQueue, generator_func=fibonacci)
    factorial_provider = providers.Factory(GeneratorQueue, generator_func=factorial)
    powers_of_two_provider = providers.Factory(GeneratorQueue, generator_func=powers_of_two)
    random_numbers_provider = providers.Factory(GeneratorQueue, generator_func=random_numbers)

    # Генераторы алфавитов и дней недели
    alphabet_provider = providers.Factory(GeneratorQueue, generator_func=alphabet)
    reverse_alphabet_provider = providers.Factory(GeneratorQueue, generator_func=reverse_alphabet)
    russian_alphabet_provider = providers.Factory(GeneratorQueue, generator_func=russian_alphabet)
    reverse_russian_alphabet_provider = providers.Factory(
        GeneratorQueue, generator_func=reverse_russian_alphabet
    )
    days_of_week_provider = providers.Factory(GeneratorQueue, generator_func=days_of_week)

    # Форматированные строки
    decimal_strings_provider = providers.Factory(
        GeneratorQueue, generator_func=lambda: formatted_decimal_strings(2)
    )
    thousandth_strings_provider = providers.Factory(
        GeneratorQueue, generator_func=lambda: formatted_decimal_strings(3)
    )
    ten_thousandth_strings_provider = providers.Factory(
        GeneratorQueue, generator_func=lambda: formatted_decimal_strings(4)
    )
