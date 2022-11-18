#!/bin/bash
# !/usr/bin/python3


tuple_old = (9, 10, 21, 36, 27, 55, 90, 99, 999)

lst_new = []
for i in tuple_old:
    sum_j = (sum(map(int, str(i))))  # Сумма цифр каждого числа
    if sum_j % 9 == 0:
        lst_new.append(i)

print("Решение циклом и условием: ", lst_new)


lst_new_func = list(filter(lambda x: (sum(map(int, str(x)))) % 9 == 0, tuple_old))
print("Решение функцией lambda: ", lst_new_func)
