#!/bin/bash
# !/usr/bin/python3

string_1, string_2, string_3, string_4 = input("Вести строку 1: "), input("Вести строку 2: "), input(
    "Вести строку 3: "), input("Вести строку 4: ")

arg_1 = string_1 + "|\n" + string_2 + "|\n"

file = open("Task_2.txt", "w+", encoding='utf-8')  # Создание внешнего файла и запись в него результата
file.write(arg_1)
file.close()

with open("Task_2.txt", "a+", encoding='utf-8') as file:
    file.write(string_3.upper() + '|\n')
    file.write(string_4.upper() + '|\n')

with open("Task_2.txt", "r", encoding='utf-8') as file:
    result = file.read()
    print(result)
