#!/bin/bash
# !/usr/bin/python3


def start(res):
    s = input("Выберите вариант работы: \n 1 - Добавить новый словарь, \n 2 - Останов скрипта \n")
    if s == "1":
        add_dict(res)
    elif s == "2":
        exit()
    else:
        print("Сделайте правильный выбор")
        start()


def add_dict(dict_res):
    dict_new = {input("Ввести ключ: "): int(input("Ввести значение: ")) for _ in
                range(int(input("Ввести количество элементов: ")))}

    for key, value in dict_new.items():
        if key in dict_res.keys():
            dict_res[key] = value + dict_res[key]
        else:
            dict_res[key] = value

    print("Введенный словарь: ", dict_new)
    print("Результат сложения: ", dict_res)
    start(dict_res)


result = dict()

start(result)
