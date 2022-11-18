#!/bin/bash
# !/usr/bin/python3

print("Обрабатываемая строка: ", b'r\xc3\xa9sum\xc3\xa9')

s = b'r\xc3\xa9sum\xc3\xa9'.decode()

print("Декодированная строка:", s)
print("Строка в кодировке 'utf-8': ", s.encode('utf8'))
print("Строка в кодировке 'utf-8' и декодировке 'utf-16': ", s.encode('utf8').decode('utf-16'))
