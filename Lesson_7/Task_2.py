#!/bin/bash
# !/usr/bin/python3


lst_old = ["123321", "ротондра", "123456", "78987"]

lst_new = list(filter(lambda x: x == x[::-1], lst_old))

print("Палиндромы: ", *lst_new)
