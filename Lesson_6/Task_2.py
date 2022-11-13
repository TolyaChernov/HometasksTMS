#!/bin/bash
# !/usr/bin/python3


def start():
    s = input("Введите произвольную строку: ")
    if s != "":
        replace_str(s)
    else:
        start()


def replace_str(my_str):
    new_str = []
    for i in my_str:
        if i == "\"":
            new_str.append("\'")
        elif i == "'":
            new_str.append("\"")
        else:
            new_str.append(i)
    print("".join(new_str))


start()
