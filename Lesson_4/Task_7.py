# !/bin/bash
# !/usr/bin/python3

words = input("Введите строку: ")
n = input("Введите число: ")
try:
    n = int(n)
except ValueError:
    print("Проверьте правильность ввода числа")
    quit()
symb = input("Введите произвольный символ: ")

w = []
for i in range(len(words)):
    if i > 0 and i % 2 == 0:
        w.append(words[i] + symb * n)
    else:
        w.append(words[i])
print(words, "\n", *w, sep="", end="\n" + symb * n)
