#!/bin/bash
# !/usr/bin/python3


def get_digits(my_num: int) -> tuple:
    tup = tuple(str(my_num))
    return tup


num = int(input("Заданное целое число: "))
res = get_digits(num)
print("Полученный кортеж: ", res)
