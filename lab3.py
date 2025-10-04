#Задание 1
list_1 = [x ** 2 for x in range(1,11)]
print(f"Квадраты чисел от 1 до 10: {list_1}")

#Задание 2
list_2 = [x for x in range(1,20) if x % 2 == 0]
print(f"Чётные числа от 1 до 20: {list_2}")

#Задание 3
words = ["python", "Java", "c++", "Rust", "go"]
list_3 = [_.upper() for _ in words if len(_) > 3]
print(f"Отфильтрованные слова: {list_3}")

#Задание 4
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Пример использования
print("Countdown от 5:")
for x in Countdown(5):
    print(x, end=" ")
print()