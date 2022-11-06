# !/bin/bash
# !/usr/bin/python3

# Сумма цифр числа

a = input("Введите число: ").strip()

# Проверка на число
if a.isnumeric():
    a = int(a)
else:
    print("Введенная строка не является числом")
    quit()

total = 0

while a > 0:
    total += a % 10
    a //= 10

print("Сумма цифр введенного числа:", total)
