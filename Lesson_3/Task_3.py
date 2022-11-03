#!/bin/bash
# !/usr/bin/python3

x, y = float(input("Введите число x: ")), float(input("Введите число y: "))
print((abs(x) - abs(y)) / (1 + abs(x * y)))
