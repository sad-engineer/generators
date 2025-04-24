#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------------------
"""Модуль со строковыми генераторами."""

from typing import Generator


def alphabet() -> Generator[str, None, None]:
    """Генератор букв латинского алфавита."""
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        yield letter


def reverse_alphabet() -> Generator[str, None, None]:
    """Генератор букв латинского алфавита в обратном порядке (Z, Y, X, ...)."""
    for letter in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        yield letter


def russian_alphabet() -> Generator[str, None, None]:
    """Генератор букв русского алфавита."""
    for letter in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
        yield letter


def reverse_russian_alphabet() -> Generator[str, None, None]:
    """Генератор букв русского алфавита в обратном порядке."""
    for letter in reversed("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"):
        yield letter


def days_of_week() -> Generator[str, None, None]:
    """Генератор дней недели (Понедельник, Вторник, ...)."""
    days = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
    ]
    index = 0
    while True:
        yield days[index]
        index = (index + 1) % 7
