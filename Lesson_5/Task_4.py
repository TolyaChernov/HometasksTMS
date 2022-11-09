#!/bin/bash
# !/usr/bin/python3

import random

n = random.randint(1, 100)

print(f"Подсказка: {n}")

while True:
    n_new = input("Угадайте число ('stop' остановит игру): ")
    if n_new == "stop":
        print("Игра остановлена")
        exit()

    if n != int(n_new):
        print("Попробуйте угадать еще раз")
    else:
        print(f"Поздравляю! Вы угадали число: {n}")
        break
