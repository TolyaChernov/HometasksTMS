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
        """Метод остановки"""
        self.age += 1
        print(f"Age {self.brand} is {self.age} years old")


# Проверка результатов
car_1 = Auto("BMW", 9, 5)
car_1.color = "red"
car_2 = Auto("Audi", 14, 4)
car_2.weight = 2500

print(car_1.brand, car_1.age, car_1.mark, car_1.color, car_1.weight)
car_1.drive()
car_1.stop()
car_1.use()
car_1.use()

print()

print(car_2.brand, car_2.age, car_2.mark, car_2.color, car_2.weight)
car_2.drive()
car_2.stop()
car_2.use()
car_2.use()

