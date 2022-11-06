# !/bin/bash
# !/usr/bin/python3

words = input("Введите строку: ").strip().lower()
assert words.count(" ") >= 2, "Должно быть не менее 3-х слов"

lst = words.split()

lst[0] = lst[0].title()
lst[-1] = lst[-1].title()

print(*lst)
