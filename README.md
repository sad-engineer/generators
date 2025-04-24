# generators

`generators` - это пакет Python, содержащий различные генераторы последовательностей.

Материал демонстрационный, показывает навыки работы с:
- интерфейсами (typing.Protocol),
- dependency_injector (containers, providers)

## Установка

Для установки пакета используйте команду:

```sh
pip install git+https://github.com/sad-engineer/generators.git
```

## Клонирование проекта

Для клонирования проекта используйте команду:

```sh
git clone https://github.com/sad-engineer/generators.git
cd generators
```

## Использование
Примеры работы с генераторами в файле example.py

### Базовые примеры

```python
from generators import GeneratorQueue, positive_numbers, alphabet

# Создание генератора положительных чисел
numbers = GeneratorQueue(positive_numbers)
print(numbers.current_value)  # 1
print(numbers.next_value)     # 2
print(numbers.next_value)     # 3
print(numbers.previous_value) # 2

# Создание генератора букв алфавита
letters = GeneratorQueue(alphabet)
print(letters.current_value)  # A
print(letters.next_value)     # B
print(letters.next_value)     # C
print(letters.previous_value) # B
```

### Пример с навигацией по истории

```python
from generators import GeneratorQueue, days_of_week

# Создание генератора дней недели
days = GeneratorQueue(days_of_week)

# Получаем несколько значений
print(days.current_value)     # Понедельник
print(days.next_value)        # Вторник
print(days.next_value)        # Среда
print(days.next_value)        # Четверг

# Возвращаемся назад
print(days.previous_value)    # Среда
print(days.previous_value)    # Вторник

# Снова вперед
print(days.next_value)        # Среда

# Сбрасываем генератор
print(days.reset_value)       # Понедельник
```

### Пример с числовыми последовательностями

```python
from generators import GeneratorQueue, fibonacci, factorial

# Генератор чисел Фибоначчи
fib = GeneratorQueue(fibonacci)
print(fib.current_value)  # 0
print(fib.next_value)     # 1
print(fib.next_value)     # 1
print(fib.next_value)     # 2
print(fib.next_value)     # 3

# Генератор факториалов
fact = GeneratorQueue(factorial)
print(fact.current_value) # 1
print(fact.next_value)    # 2
print(fact.next_value)    # 6
print(fact.next_value)    # 24
```

### Пример со строковыми генераторами

```python
from generators import GeneratorQueue, russian_alphabet, reverse_russian_alphabet

# Русский алфавит
rus = GeneratorQueue(russian_alphabet)
print(rus.current_value)  # А
print(rus.next_value)     # Б
print(rus.next_value)     # В

# Русский алфавит в обратном порядке
rev_rus = GeneratorQueue(reverse_russian_alphabet)
print(rev_rus.current_value)  # Я
print(rev_rus.next_value)     # Ю
print(rev_rus.next_value)     # Э
```

## Структура проекта
```
generators/
├── generators/                 # Основной пакет
│   ├── __init__.py             # Инициализация пакета
│   ├── container.py            # Контейнер для управления генераторами
│   ├── example.py              # Примеры использования
│   ├── generator_queue.py      # Очередь генераторов с историей
│   ├── interfaces.py           # Интерфейсы генераторов
│   ├── numeric_generators.py   # Числовые генераторы
│   └── string_generators.py    # Строковые генераторы
├── pyproject.toml              # Конфигурация проекта
├── requirements.txt            # Зависимости проекта
├── setup.py                    # Настройки установки
└── README.md                   # Документация
```

## Требования

- Python 3.9 или выше
- dependency-injector 4.46.0 или выше

## Установка зависимостей

Для установки зависимостей проекта можно использовать pip или Poetry:

### Установка через pip

```sh
# Создайте виртуальное окружение
python -m venv venv

# Активируйте виртуальное окружение
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate

# Установите зависимости
pip install -r requirements.txt
```

### Установка через Poetry

1. Установите Poetry, если он еще не установлен:
```sh
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# Linux/MacOS
curl -sSL https://install.python-poetry.org | python3 -
```

2. Установите зависимости проекта:
```sh
# Перейдите в директорию проекта
cd generators

# Установите зависимости
poetry install

# Активируйте виртуальное окружение
poetry shell
```

## Версии

- 0.0.1 - Текущая версия
- Поддержка числовых и строковых генераторов
- Очередь генераторов с историей значений
- Контейнер для управления генераторами

## Вклад в проект

1. Создайте форк проекта
2. Создайте ветку для ваших изменений
3. Внесите изменения
4. Отправьте pull request

Пожалуйста, убедитесь, что ваши изменения:
- Сопровождаются тестами
- Следуют существующему стилю кода
- Обновляют документацию при необходимости
