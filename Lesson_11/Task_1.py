"""Скрипт решения домашнего задания №1 из лекции №11"""


class Food:
    """Класс Блюдо"""

    food_list = []

    def __init__(self, count: int = 1, name: str = "Noname", price: float = 0, mass: float = 0):
        """Инициализация элементов (словарей) меню"""
        self.count = count
        self.name = name
        self.price = price
        self.mass = mass
        Food.food_list.append(self)  # Список из пунктов меню (список словарей)


# Формирование меню
bludo_1 = Food(1, "Форель отварная", 12.50, 500)
bludo_2 = Food(1, "Форель жаренная", 15.90, 450)
bludo_3 = Food(1, "Форель недожаренная", 13.40, 470)
bludo_4 = Food(1, "Форель пережаренная", 17.40, 350)
bludo_5 = Food(1, "Форель тушеная", 14.15, 650)
bludo_6 = Food(1, "Форель какая-нибудь", 17.15, 750)


class Zakaz(Food):
    """Класс по работе с заказами"""

    zakaz_1 = {}
    zakaz_2 = []

    @classmethod
    def zakaz_add(cls, bludo, count_z=1):
        """Функция формирования листа заказа согласно меню"""
        cls.zakaz_1[bludo] = count_z

    @classmethod
    def chek(cls):
        """Функция вывода счета"""
        number = 0
        weight = 0
        price_check = 0
        for key, value in cls.zakaz_1.items():
            for item in Food.food_list:
                if item.name == key:
                    cls.zakaz_2.append(
                        f"{item.name}, {value} шт., {round(item.price * value, 3)} р., {item.mass * value} гр.")
                    print(f"{item.name}, {value} шт., {round(item.price * value, 3)} р., {item.mass * value} гр.")
                    number += value
                    weight += item.mass * value
                    price_check += item.price * value
        print(f"ИТОГО:          {number} шт., {round(price_check, 3)} р., {weight} гр.")
        return cls.zakaz_2, price_check

    @classmethod
    def prepay(cls, pay, money):
        """Расчет окончательной стоимости с учетом предоплаты"""
        if pay - money > 0:
            print("\nВнесена предоплата в размере: ", money, "р.", "\nСумма окончательного расчета: ",
                  round(pay - money, 2), "р.")
        elif pay == money:
            print("\nВнесена предоплата в размере: ", money, "р.", "\nСумма окончательного расчета: ",
                  abs(round(pay - money, 2)), "р.", "\nСчет закрыт")
        else:
            print("\nВнесена предоплата в размере: ", money, "р.", "\nСумма возврата : ", abs(round(pay - money, 2)),
                  "р.")

        # return round(pay - money, 2)


# Ввод заказанных блюд
Zakaz.zakaz_add("Форель жаренная")
Zakaz.zakaz_add("Форель отварная", 5)
Zakaz.zakaz_add("Форель тушеная", 4)
Zakaz.zakaz_add("Форель какая-нибудь", 6)

# print(Zakaz.zakaz_1)

# Вывод счета
*arg, price = Zakaz.chek()

# Предоплата
pre_pay = 237.9

# Итоговая стоимость с учетом предоплаты
Zakaz.prepay(price, pre_pay)

