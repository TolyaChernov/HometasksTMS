#!/bin/bash
#!/usr/bin/python3

words = input("Введите первое слово: ")
symbol = input("Введите второе слово: ")

print("итоговая строка: ", words[1:-1] + symbol[-2:0:-1])