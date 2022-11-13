#!/bin/bash
# !/usr/bin/python3


def w_factorial(n):
    if n == 0:
        return 1
    else:
        return n * w_factorial(n - 2)


input_number = int(input("Введите число: "))

res = w_factorial(input_number)
print(res)
