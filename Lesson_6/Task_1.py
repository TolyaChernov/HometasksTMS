#!/bin/bash
# !/usr/bin/python3


def start():
    s = input("Выберите вариант работы: \n 1 - ввести новый словарь, \n 2 - использовать подготовленный словарь \n")
    if s == "1":
        new_dict()
    elif s == "2":
        my_dict()
    else:
        print("Сделайте правильный выбор")
        start()


def new_dict():
    d1 = {input("Ввести ключ: "): int(input("Ввести значение: ")) for _ in
          range(int(input("Ввести количество элементов: ")))}
    d2 = {value: key for key, value in d1.items()}
    print("Введенный словарь: ", d1)
    print("Результат изменений: ", d2)


def my_dict():
    d1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    d2 = {value: key for key, value in d1.items()}
    print("Подготовленный словарь: ", d1)
    print("Результат изменений: ", d2)


start()
