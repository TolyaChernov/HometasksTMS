#!/bin/bash
# !/usr/bin/python3

"""
4. Реализуйте функцию, которая получает список из целых чисел, и возвращает
новый список, в котором каждый элемент с индексом i нового списка является
суммой всех чисел в исходном списке, кроме числа i.
>>> foo([1, 2, 3, 4, 5])
[14, 13, 12, 11, 10]

>>> foo([3, 2, 1])
[3, 4, 5]
"""


def foo(num: list) -> list:
    lst_new = []
    for i in range(len(num)):
        total = 0
        for j in range(len(num)):
            if j != i:
                total += num[j]
            else:
                continue
        lst_new.append(total)
    return lst_new


lst = [int(input("Ввести значение: ")) for i in range(int(input("Ввести количество элементов: ")))]
print("Список из чисел: ", lst)

res = foo(lst)
print("Новый список: ", res)
