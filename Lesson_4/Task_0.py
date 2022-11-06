# !/bin/bash
# !/usr/bin/python3

a, b = input("Введите переменную a: "), input("Введите переменную b: ")
a, b = b, a
print(f"Переменная a = {a}", f"Переменная b = {b}", sep="\n")
