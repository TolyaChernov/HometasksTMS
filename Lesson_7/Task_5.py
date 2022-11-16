#!/bin/bash
# !/usr/bin/python3

import functools


def remember_result(func):
    @functools.wraps(func)
    def wrapper(*args):
        try:  # Попытка открыть внешний файл с предыдущим значением
            file = open("name_.txt", "r+")
            res = file.read()
            file.close()
        except FileNotFoundError:  # Присвоение значения в случае отсутствия файла
            res = "None"
        if res == '':  # Присвоение значение в случае пустого файла
            res = "None"
        print(f"Last result = '{res}'")

        file = open("name_.txt", "w+")  # Создание внешнего файла и запись в него результата
        file.write(func(*args))
        file.close()

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


sum_list('45', '50006', 'df000')
