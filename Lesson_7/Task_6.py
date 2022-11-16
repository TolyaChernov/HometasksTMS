#!/bin/bash
# !/usr/bin/python3


tuple_old = (9, 10, 21, 36, 27, 55, 90, 99, 999)

# n = list(tuple_old)
lst_new = []
for i in tuple_old:
    sum_j = (sum(map(int, str(i))))  # Сумма цифр каждого числа
    if sum_j % 9 == 0:
        lst_new.append(i)

print(lst_new)
