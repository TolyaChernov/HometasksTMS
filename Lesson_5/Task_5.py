#!/bin/bash
# !/usr/bin/python3


n = input("Введите строку: ")

s = list(set(n))

d = {i: n.count(i) for i in s}

print(d)
