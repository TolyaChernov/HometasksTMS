#!/bin/bash
# !/usr/bin/python3


def my_split(new_string, new_sep=[]):
    if new_sep == "":
        new_sep = " "

    res_string = []
    start = 0

    for i in range(len(new_string)):
        if i == new_string.find(new_sep, i, len(new_string)):
            finish = i
            res_string.append(new_string[start:finish].strip())
            start = i + len(new_sep)
    res_string.append(new_string[start:len(new_string)].strip())
    print(res_string)


input_string = input("Введите произвольную строку: ").strip()
input_sep = input("Символ разделения: ")

my_split(input_string, input_sep)
