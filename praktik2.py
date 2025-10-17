"""Практическая работа 2."""


def logger(func):
    def wrapper(*args, **kwargs):
        # Перед вызовом функции
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        
        # Выполнение функции
        result = func(*args, **kwargs)
        
        # После выполнения функции
        print(f"Функция {func.__name__} вернула {result}")
        
        return result
    return wrapper

# Применяем декоратор к функциям


@logger
def add(a, b):
    """Возвращает сумму двух чисел"""
    return a + b


@logger
def divide(a, b):
    """Возвращает результат деления"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"


@logger
def greet(name):
    """Выводит приветствие"""
    return f"Привет, {name}!"


# Тестируем функции с логированием
print("=== Тестирование декоратора логирования ===")
add(5, 3)
print()

divide(10, 2)
print()

divide(10, 0)
print()

greet("Анна")
print()