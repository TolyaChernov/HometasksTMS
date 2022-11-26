"""Скрипт решения домашнего задания №2 из лекции №10"""
import time

class Auto:
    """Класс авто"""
    color = "black"
    weight = 2000

    def __init__(self, brand, age, mark):
        """Инициализация автомобиля"""
        self.brand = brand
        self.age = age
        self.mark = mark

    def drive(self):
        """Метод движения"""
        print(f"Car {self.brand} {self.mark} drives")

    def stop(self):
        """Метод остановки"""
        print(f"Car {self.brand} {self.mark} stops")

    def use(self):
        """Метод использования"""
        self.age += 1
        print(f"Age {self.brand} is {self.age} years old")


class Truck(Auto):
    """Дочерний класс Truck"""
    max_load = 11

    def drive(self):
        """Переопределенный метод движения дочернего класса Truck"""
        print("Attention!")
        print(f"Car {self.brand} {self.mark} drives")

    def load(self):
        """Метод загрузки"""
        time.sleep(1)  # задержка в течение 1 секунды
        print("Load")
        time.sleep(1)  # задержка в течение 1 секунды


class Sedan(Auto):
    """Дочерний класс Sedan"""
    max_speed = 160

    def drive(self):
        """Переопределенный метод движения дочернего класса Sedan"""
        print(f"Car {self.brand} {self.mark} drives")
        print(f"max speed of sedan {self.brand} {self.mark} is {self.max_speed}")


# Проверка результатов
truck_1 = Truck("Volvo", 50, 20)
print(truck_1.brand, truck_1.age, truck_1.mark, truck_1.color, truck_1.weight)
truck_1.drive()
truck_1.load()
truck_1.use()
print()

truck_2 = Truck("MAZ", 10, 8)
print(truck_2.brand, truck_2.age, truck_2.mark, truck_2.color, truck_2.weight)
truck_2.drive()
truck_2.load()
truck_2.use()

