#!/bin/bash
# !/usr/bin/python3

name, age = input("Введите Ваше имя: "), int(input("Введите Ваш возраст: "))

if age >= 18:
    print(f"Уважаемый {name}, добро пожаловать на сайт!")
else:
    print(f"Уважаемый {name}, доступ на сайт ограничен!")
