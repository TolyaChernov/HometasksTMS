"""Скрипт решения домашнего задания №2 из лекции №11"""

from abc import ABC, abstractmethod


class Interface_temp(ABC):

    def setTemp(self, temp):
        self.temp = temp

    def setTemp(self, temp):
        self.temp = temp

    @abstractmethod
    def letsgo(self):
        pass


class Cel(Interface_temp):

      def letsgo(self):
        print(f"{temp}°C == {temp + 273.15}°K == {round(temp * 9 / 5 + 32, 3)}°F ")
        return temp, temp + 273.15, round(temp * 9 / 5 + 32, 3)


class Kel(Interface_temp):

      def letsgo(self):
        print(f"{round(temp - 273.15, 3)}°C == {temp}°K == {round((temp - 273.15) * 9 / 5 + 32, 3)}°F ")
        return round(temp - 273.15, 3), temp, round(temp * 9 / 5 + 32, 3)


class Far(Interface_temp):

    def letsgo(self):
        print(f"{round((temp - 32) * 5 / 9, 3)}°C == {round((temp - 32) * 5 / 9 + 273.15, 3)}°K == {temp}°F ")
        return round((temp - 32) * 5 / 9, 3), round((temp - 32) * 5 / 9 + 273.15, 3), temp


choise = int(input("Выбрать вариант шкалы для ввода:\n 1. Цельсия\n 2. Кельвина\n 3. Фаренгейта\n(Выбрать 1 - 3): "))

if choise == 1:
    temper = Cel()
elif choise == 2:
    temper = Kel()
elif choise == 3:
    temper = Far()

temp = float(input("Ввести температуру для конвертации: "))
temper.setTemp(temp)
temper.letsgo()

