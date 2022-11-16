#!/bin/bash
# !/usr/bin/python3


import datetime


def log_function(func):
    def wrapper(arg_1, arg_2):
        print(
            f"Вывод: {datetime.datetime.now()} | Function: {func.__name__} | "
            f"Expected: 'a': {type(arg_1)}, 'b': {type(arg_2)} | Input: ({arg_1}, '{arg_2}')")
        func(arg_1, arg_2)

    return wrapper


@log_function
def test(a: int, b: str):
    print(a, b)


try:
    it_1 = int(input("Аргумент 1 (число): "))
except ValueError:
    print("Должно быть число")
    exit()
it_2 = str(input("Аргумент 2 (строка): "))

test(it_1, it_2)
