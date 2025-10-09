#Задание 1
class Transport:
    def __init__(self, brand, speed):
        self.brand = brand  # марка
        self.speed = speed  # скорость
    
    def move(self):
        print(f"Транспорт движется со скоростью {self.speed} км/ч")
    
    def __str__(self):
        return f"Транспорт: {self.brand}, Скорость: {self.speed}"

#Задание 2 + 3
class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats  # количество мест
    
    def honk(self):
        print("Бип бип!")  # гудок
    
    def move(self):
        print(f"Автомобиль {self.brand} едет со скоростью {self.speed} км/ч")
    
    def __str__(self):
        return f"Автомобиль: {self.brand}, Скорость: {self.speed}, Мест: {self.seats}"
    
    def __len__(self):
        return self.seats  # возвращает количество мест
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed  # сравнение по скорости
        return False
    
    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed  # суммарная скорость
        return NotImplemented

class Bike(Transport):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type  # тип велосипеда
    
    def move(self):
        print(f"Велосипед {self.brand} едет со скоростью {self.speed} км/ч")
    
    def __str__(self):
        return f"Велосипед: {self.brand}, Скорость: {self.speed}, Тип: {self.type}"

# Задание 4
# Использование классов
# Создание объектов разных классов
transport = Transport("Generic", 50)  # базовый транспорт
car1 = Car("Toyota", 120, 5)         # автомобиль 1
car2 = Car("Honda", 120, 4)          # автомобиль 2
bike = Bike("Trek", 30, "mountain")  # велосипед

# Вывод объектов на экран (используется __str__)
print("Вывод объектов:")
print(transport)
print(car1)
print(car2)
print(bike)
print()  

# Проверка работы методов move()
print("Проверка методов move():")
transport.move()
car1.move()
car2.move()
bike.move()
print()  

# Проверка метода honk() для автомобиля
print("Проверка метода honk() для автомобиля:")
car1.honk()
print() 

# Использование len(car) для автомобиля
print("Количество мест в car1:", len(car1))
print()

# Сравнение двух автомобилей (car1 == car2)
print("Сравнение car1 == car2:", car1 == car2)
print()  

# Сложение скоростей двух автомобилей (car1 + car2)
print("Суммарная скорость car1 + car2:", car1 + car2)
print()  

# Попытка сложить автомобиль и велосипед (car1 + bike)
print("Попытка сложить автомобиль и велосипед:")
try:
    result = car1 + bike
    print("Суммарная скорость car1 + bike:", result)
except TypeError as e:
    print("Ошибка при сложении car1 + bike:", e)
print() 

# Создание списка объектов и вызов метода move() для каждого
vehicles = [transport, car1, car2, bike]
print("Вызов метода move() для всех объектов в списке:")
for vehicle in vehicles:
    vehicle.move()