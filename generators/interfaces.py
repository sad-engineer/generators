#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
"""Модуль с интерфейсами для генераторов."""

from typing import Any, Generator, Protocol


class IGenerator(Protocol):
    """Протокол для генераторов."""

    def __iter__(self) -> Generator[Any, None, None]:
        """Возвращает генератор значений."""
        ...


class IGeneratorQueue(Protocol):
    """Протокол для очереди генераторов."""

    @property
    def current_value(self) -> Any:
        """Возвращает текущее значение."""
        ...

    @property
    def next_value(self) -> Any:
        """Возвращает следующее значение."""
        ...

    @property
    def previous_value(self) -> Any:
        """Возвращает предыдущее значение."""
        ...

    def reset(self) -> None:
        """Сбрасывает генератор в начальное состояние."""
        ...

    def get_current_value(self) -> Any:
        """Возвращает текущее значение генератора (как метод)."""
        ...

    def get_next_value(self) -> Any:
        """Возвращает следующее значение генератора (как метод)."""
        ...

    def get_previous_value(self) -> Any:
        """Возвращает предыдущее значение генератора (как метод)."""
        ...

    def get_reset_value(self) -> Any:
        """Сбрасывает значение генератора (как метод)."""
        ...
