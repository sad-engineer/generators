#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
"""Модуль с очередью генераторов."""

from typing import Any, Callable, Generator

from generators.interfaces import IGeneratorQueue


class GeneratorQueue(IGeneratorQueue):
    """
    Класс-обертка для генераторов с историей всех значений.
    Позволяет перемещаться по истории значений в обе стороны.
    """

    def __init__(self, generator_func: Callable[[], Generator[Any, None, None]]):
        """
        Инициализация обертки.

        :param generator_func: Функция, создающая генератор (не сам генератор, а функция!)
        """
        self.generator_func = generator_func  # Поле для хранения генераторной функции
        self._reset_generator()  # Инициализируем генератор

    def _reset_generator(self) -> None:
        """Сбрасывает генератор в начальное состояние."""
        self.generator = self.generator_func()  # Пересоздаем генератор
        self._history = [next(self.generator)]  # Начинаем с первого значения
        self._current_index = 0  # Сбрасываем индекс

    @property
    def current_value(self) -> Any:
        """Возвращает текущее значение генератора."""
        return self._history[self._current_index]

    def get_current_value(self) -> Any:
        """Возвращает текущее значение генератора (как метод)."""
        return self.current_value

    @property
    def next_value(self) -> Any:
        """Переходит к следующему значению, если оно есть, иначе запрашивает новый."""
        if self._current_index + 1 < len(self._history):
            # Если следующий элемент уже есть в истории — просто переходим к нему
            self._current_index += 1
        else:
            # Если следующего элемента нет — запрашиваем новый у генератора
            self._history.append(next(self.generator))
            self._current_index += 1
        return self._history[self._current_index]

    def get_next_value(self) -> Any:
        """Возвращает следующее значение генератора (как метод)."""
        return self.next_value

    @property
    def previous_value(self) -> Any:
        """Переходит к предыдущему значению, если возможно, иначе бросает ValueError."""
        if self._current_index > 0:
            self._current_index -= 1
            return self._history[self._current_index]
        raise ValueError('Предыдущего элемента не существует')

    def get_previous_value(self) -> Any:
        """Возвращает предыдущее значение генератора (как метод)."""
        return self.previous_value

    @property
    def reset_value(self) -> Any:
        """Сбрасывает текущее значению."""
        self._reset_generator()
        return self.current_value

    def get_reset_value(self) -> Any:
        """Сбрасывает значение генератора (как метод)."""
        return self.reset_value
