#!/bin/bash
# !/usr/bin/python3


lst_old = ["ryewuiiwuery", "ротондра", 'sdffds', '45654']

lst_new = list(map(list, lst_old))
print("Результат работы функции map:", lst_new)


def analog_func(*args):
    lst_new_1 = []
    args_new = list(*args)
    for i in args_new:
        buf = []
        for j in i:
            # print(j)
            buf.append(j)
        lst_new_1.append(buf)
    print("Результат работы аналогичной функции:", lst_new_1)
    return lst_new_1


analog_func(lst_old)
