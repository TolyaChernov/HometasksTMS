#!/bin/bash
# !/usr/bin/python3


tuple_old = (1, 2, 3, 9, 10, 21, 36, 27, 55, 90, 99, 999)

tuple_new = tuple(filter(lambda x: x % 9 == 0, tuple_old))

print(tuple_new)
