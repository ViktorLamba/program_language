"""laboratory 2"""
import random

def exercise_1():
    """Number 1-5"""
    #Задание 1
    print("Задание 1")
    print("Таблица умножения:")
    print("     ", end="")
    for i in range(1, 10):
        print(f"{i:4}",end="")
    print("\n" + "-" * 40)
    for i in range(1, 10):
        print(f"{i:2} |", end="")
        for j in range(1, 10):
            print(f"{i * j:4}", end="")
        print()

    #Задание 2
    print("Задание 2")
    sum_odd = 0
    for i in range(1, 101, 2):
        sum_odd += i
    print(f"Сумма нечётных чисел от 1 до 100: {sum_odd}")

    #Задание 3
    print("Задание 3")
    n = int(input("Введите число: "))
    print(f"Делители числа {n}:", end=" ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()

    #Задание 4
    print("Задание 4")
    print("\n" + "=" * 50)
    n = int(input("Введите число: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Факториал числа {n} = {factorial}")

    #Задание 5
    print("Задание 5")
    n = int(input("Введите длину последовательности: "))
    fib = [0, 1]
    if n <= 0:
        print("Длина должна быть положительным числом")
    elif n == 1:
        fib = [0]
    else:
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
    print("Последовательность:", " ".join(map(str, fib)))


def exercise_2():
    """Number 1-5"""
    numbers = [random.randint(-50, 50) for _ in range(10)]
    print(f"Исходный список: {numbers}")
    print("=" * 50)

    # 1. Чётные элементы
    print("Задание 1")
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    print(f"Чётные числа: {even_numbers}")
    print()

    # 2. Максимальное и минимальное число
    print("Задание 2")
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print(f"Максимальное: {max_num}")
    print(f"Минимальное: {min_num}")
    print()

    # 3. Ввод 5 чисел от пользователя
    print("Задание 3")
    user_numbers = []
    for i in range(5):
        num = int(input(f"Введите число {i + 1}: "))
        user_numbers.append(num)
    user_numbers.sort()
    print(f"Отсортированный список: {user_numbers}")
    print()

    # 4. Удаление дубликатов
    print("Задание 4")
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    print(f"Список без дубликатов: {unique_numbers}")
    print()

    # 5. Поменять местами первый и последний элемент
    print("Задание 5")
    if len(numbers) >= 2:
        first = numbers[0]
        last = numbers[-1]
        numbers[0] = last
        numbers[-1] = first
    print(f"Список после замены: {numbers}")


def exercise_3():
    """Number 1-4"""
    # 1. Словарь студентов и средний балл
    print("Задание 1")
    students = {
        "Иван": 10,
        "Мария": 12,
        "Петр": 18,
        "Анна": 100,
        "Сергей": 90
    }
    print("Оценки студентов:")
    for name, grade in students.items():
        print(f"{name}: {grade}")
    average_grade = sum(students.values()) / len(students)
    print(f"Средний балл: {average_grade:.2f}")
    print()

    # 2. Подсчет букв в строке
    print("Задание 2")
    text = input("Введите строку: ").lower()
    letter_count = {}
    for char in text:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    print("Количество каждой буквы:")
    for letter, count in sorted(letter_count.items()):
        print(f"'{letter}': {count}")
    print()

    # 3. Словарь чисел и их квадратов
    print("Задание 3")
    squares_dict = {i: i ** 2 for i in range(1, 11)}
    print("Числа и их квадраты:")
    for number, square in squares_dict.items():
        print(f"{number}² = {square}")
    print()

    # 4. Словарь из двух списков
    print("Задание 4")
    keys = ["имя", "возраст", "город", "профессия"]
    values = ["Алексей", 25, "Москва", "инженер"]
    if len(keys) == len(values):
        combined_dict = dict(zip(keys, values))
        print("Полученный словарь:")
        for key, value in combined_dict.items():
            print(f"{key}: {value}")
    else:
        print("Ошибка: списки разной длины!")


def exercise_4():
    """Number 1-5"""
    # 1. Пересечение и объединение множеств
    print("Задание 1")
    set1 = {1, 2, 3, 4, 5, 6}
    set2 = {4, 5, 6, 7, 8, 9}
    print(f"Множество 1: {set1}")
    print(f"Множество 2: {set2}")
    print(f"Пересечение: {set1 & set2}")
    print(f"Объединение: {set1 | set2}")
    print(f"Разность (set1 - set2): {set1 - set2}")
    print(f"Симметрическая разность: {set1 ^ set2}")
    print()

    # 2. Уникальные слова в тексте
    print("Задание 2")
    text = input("Введите текст: ").lower()
    words = text.split()
    word_count = {}  # Словарь для подсчета количества слов
    for word in words:
        cleaned_word = word.strip('.,!?;:"()')
        if cleaned_word:
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
    unique_words = {word for word, count in word_count.items() if count == 1}
    print(f"Уникальные слова (встречаются только 1 раз): {sorted(unique_words)}")
    print(f"Количество уникальных слов: {len(unique_words)}")
    print()

    # 3. Общие элементы двух списков
    print("Задание 3")
    list1 = [1, 2, 3, 4, 5, 2, 3, 1]
    list2 = [4, 5, 6, 7, 8, 4, 5]
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1 & set2
    print(f"Уникальные элементы списка 1: {set1}")
    print(f"Уникальные элементы списка 2: {set2}")
    print(f"Общие элементы: {common_elements}")
    print()

    # 4. Проверка подмножества
    print("Задание 4")
    set_a = {1, 2, 3, 4, 5}
    set_b = {2, 3, 4}
    set_c = {6, 7, 8}
    print(f"Множество A: {set_a}")
    print(f"Множество B: {set_b}")
    print(f"Множество C: {set_c}")
    print(f"B ⊆ A: {set_b.issubset(set_a)}")
    print(f"C ⊆ A: {set_c.issubset(set_a)}")
    print(f"A ⊇ B: {set_a.issuperset(set_b)}")
    print(f"B ⊂ A: {set_b < set_a}")  # Строгое подмножество
    print()

    # 5. Удаление элементов меньше заданного числа
    print("Задание 5")
    numbers_set = {10, 5, 8, 15, 3, 20, 1, 25}
    print(f"Исходное множество: {numbers_set}")
    threshold = int(input("Введите число для фильтрации: "))
    temp_set = numbers_set.copy()
    temp_set = {x for x in temp_set if x >= threshold}
    print(f"Способ 2 (копия с фильтрацией): {temp_set}")
    print(f"Исходное множество не изменилось: {numbers_set}")


def exercise_5():
    """Number 1-8"""
    # 1. Уникальные значения из случайных чисел
    print("Задание 1")
    numbers = [random.randint(1, 15) for _ in range(20)]
    # Считаем количество каждого числа
    number_count = {}
    for num in numbers:
        number_count[num] = number_count.get(num, 0) + 1
    unique_numbers = {num for num, count in number_count.items() if count == 1}
    print(f"Исходный список: {numbers}")
    print(f"Уникальные значения (встречаются 1 раз): {sorted(unique_numbers)}")
    print(f"Количество уникальных: {len(unique_numbers)}")
    print()

    # 2. Словарь частот элементов
    print("Задание 2")
    frequency_dict = {}
    for num in numbers:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1
    print("Частоты элементов:")
    for num, count in sorted(frequency_dict.items()):
        print(f"{num}: {count}")
    print()

    # 3. Множество длинных слов
    print("Задание 3")
    words = ["apple", "banana", "cat", "dog", "elephant", "python", "donstu", "hi"]
    long_words = {word for word in words if len(word) > 5}
    print(f"Исходный список: {words}")
    print(f"Слова длиннее 5 символов: {long_words}")
    print()

    # 4. Частоты слов в предложении
    print("Задание 4")
    sentence = input("Введите предложение: ").lower()
    punctuation = ".,!?;:\"()[]{}<>'"
    clean_sentence = ""
    for char in sentence:
        if char not in punctuation:
            clean_sentence += char
    words_list = clean_sentence.split()
    word_freq = {}
    for word in words_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    print("Частоты слов:")
    for word, count in sorted(word_freq.items()):
        print(f"'{word}': {count}")
    print()

    # 5. Удаление дубликатов через множество
    print("Задание 5")
    numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
    unique_list = list(set(numbers_with_duplicates))
    print(f"Исходный список: {numbers_with_duplicates}")
    print(f"Без дубликатов: {sorted(unique_list)}")
    print()

    # 6. Самый дорогой товар
    print("Задание 6")
    products = {
        "яблоки": 50,
        "бананы": 80,
        "молоко": 65,
        "хлеб": 40,
        "сыр": 200,
        "колбаса": 350
    }
    most_expensive = max(products, key=products.get)
    max_price = products[most_expensive]
    print("Товары и цены:")
    for product, price in products.items():
        print(f"{product}: {price} руб.")
    print(f"\nСамый дорогой товар: {most_expensive} ({max_price} руб.)")
    print()

    # 7. Анализ повторяющихся имён
    print("Задание 7")
    names = ["Иван", "Мария", "Петр", "Анна", "Иван", "Сергей", "Мария", "Ольга", "Иван", "Мария"]
    name_count = {}
    for name in names:
        name_count[name] = name_count.get(name, 0) + 1
    repeated_names = {name for name, count in name_count.items() if count > 1}
    most_common = max(name_count, key=name_count.get)
    print(f"Список имён: {names}")
    print(f"Имена, встречающиеся более 1 раза: {repeated_names}")
    print(f"Самое частое имя: '{most_common}' ({name_count[most_common]} раза)")
    print()

    # 8. Словарь первых вхождений символов
    print("Задание 8")
    text = input("Введите строку: ")
    first_occurrence = {}
    for index, char in enumerate(text):
        if char not in first_occurrence:
            first_occurrence[char] = index
    print("Первые вхождения символов:")
    for char, index in sorted(first_occurrence.items()):
        print(f"'{char}': позиция {index}")


# exercise_1()

# exercise_2()

# exercise_3()

# exercise_4()

exercise_5()
#