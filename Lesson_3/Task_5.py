#!/bin/bash
# !/usr/bin/python3

word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

print("итоговая строка: ", word1[1:-1] + word2[-2:0:-1])
