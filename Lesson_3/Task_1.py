#!/bin/bash
# !/usr/bin/python3

a, b = float(input("Введите число a: ")), float(input("Введите число b: "))
print("1) Сумма: ", a + b, "\n",
      "2) Разность: ", a - b, "\n",
      "3) Произведение: ", a * b, "\n",
      "4) Целочисленное деление: ", a // b, "\n",
      "5) Деление по модулю: ", a % b, "\n",
      f"6) Возведение числа {a} в степень {int(b)}: ", a ** b, sep="")
