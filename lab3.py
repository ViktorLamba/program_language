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


#Задание 5
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Пример использования
print("Первые 5 чисел Фибоначчи:")
for num in fibonacci(5):
    print(num, end=" ")
print()


#Задание 6
from decimal import Decimal, ROUND_HALF_UP

def deposit_calculator():
    # Ввод данных
    initial_amount = Decimal(input("Введите начальную сумму вклада (руб): "))
    interest_rate = Decimal(input("Введите годовую процентную ставку (%): "))
    years = int(input("Введите срок вклада (лет): "))
    
    # Расчет по формуле ежемесячной капитализации
    monthly_rate = interest_rate / Decimal('12') / Decimal('100')
    months = years * 12
    
    # S = P × (1 + r/12)^(12×t)
    final_amount = initial_amount * (1 + monthly_rate) ** months
    final_amount = final_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    # Расчет прибыли
    profit = final_amount - initial_amount
    
    # Вывод результатов
    print(f"\nРезультаты расчета вклада:")
    print(f"Начальная сумма: {initial_amount} руб.")
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")

# Запуск калькулятора
deposit_calculator()