#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
"""Примеры использования генераторов."""

from generators import (
    GeneratorQueue,
    positive_numbers,
    prime_numbers,
    even_numbers,
    odd_numbers,
    square_numbers,
    cube_numbers,
    fibonacci,
    factorial,
    powers_of_two,
    random_numbers,
    alphabet,
    reverse_alphabet,
    russian_alphabet,
    reverse_russian_alphabet,
    days_of_week
)


def print_generator_values(generator: GeneratorQueue, count: int = 5) -> None:
    """Печатает указанное количество значений из генератора."""
    print(f"\nПервые {count} значений:")
    print(generator.current_value)
    for _ in range(count-1):
        print(generator.next_value)


def demonstrate_navigation(generator: GeneratorQueue) -> None:
    """Демонстрирует навигацию по значениям генератора."""
    print("\nДемонстрация навигации:")
    
    # Получаем несколько значений
    print(f"Текущее значение: {generator.current_value}")

    for _ in range(3):
        print(f"Следующее значение: {generator.next_value}")
    
    # Возвращаемся назад
    print(f"Предыдущее значение: {generator.previous_value}")
    print(f"Еще раз предыдущее значение: {generator.previous_value}")
    
    # Снова вперед
    print(f"Следующее значение: {generator.next_value}")
    
    # Сбрасываем генератор
    print(f"Сброс генератора: {generator.reset_value}")


def main():
    # Примеры с числовыми генераторами
    print("=== Числовые генераторы ===")
    
    # Положительные числа
    pos_gen = GeneratorQueue(positive_numbers)
    print_generator_values(pos_gen)
    demonstrate_navigation(pos_gen)
    
    # Простые числа
    prime_gen = GeneratorQueue(prime_numbers)
    print_generator_values(prime_gen)
    
    # Четные числа
    even_gen = GeneratorQueue(even_numbers)
    print_generator_values(even_gen)
    
    # Нечетные числа
    odd_gen = GeneratorQueue(odd_numbers)
    print_generator_values(odd_gen)
    
    # Квадраты чисел
    square_gen = GeneratorQueue(square_numbers)
    print_generator_values(square_gen)
    
    # Кубы чисел
    cube_gen = GeneratorQueue(cube_numbers)
    print_generator_values(cube_gen)
    
    # Числа Фибоначчи
    fib_gen = GeneratorQueue(fibonacci)
    print_generator_values(fib_gen)
    
    # Факториалы
    fact_gen = GeneratorQueue(factorial)
    print_generator_values(fact_gen)
    
    # Степени двойки
    pow_gen = GeneratorQueue(powers_of_two)
    print_generator_values(pow_gen)
    
    # Случайные числа
    rand_gen = GeneratorQueue(random_numbers)
    print_generator_values(rand_gen)
    
    # Примеры со строковыми генераторами
    print("\n=== Строковые генераторы ===")
    
    # Латинский алфавит
    alpha_gen = GeneratorQueue(alphabet)
    print_generator_values(alpha_gen)
    
    # Латинский алфавит в обратном порядке
    rev_alpha_gen = GeneratorQueue(reverse_alphabet)
    print_generator_values(rev_alpha_gen)
    
    # Русский алфавит
    rus_alpha_gen = GeneratorQueue(russian_alphabet)
    print_generator_values(rus_alpha_gen)
    
    # Русский алфавит в обратном порядке
    rev_rus_alpha_gen = GeneratorQueue(reverse_russian_alphabet)
    print_generator_values(rev_rus_alpha_gen)
    
    # Дни недели
    days_gen = GeneratorQueue(days_of_week)
    print_generator_values(days_gen, 7)  # Показываем все 7 дней
    demonstrate_navigation(days_gen)


if __name__ == "__main__":
    main()
