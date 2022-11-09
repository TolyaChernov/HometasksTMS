#!/bin/bash
# !/usr/bin/python3

while True:
    name = input("Введите Ваше имя (\"stop\" завершит программу): ")
    if name == "stop":
        print("Программа завершена")
        exit()
    age = int(input("Введите Ваш возраст: "))
    if age >= 18:
        print(f"Уважаемый {name}, добро пожаловать на сайт!")
    else:
        print(f"Уважаемый {name}, доступ на сайт ограничен!")
