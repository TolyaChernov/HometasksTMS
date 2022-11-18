#!/bin/bash
# !/usr/bin/python3

with open("unsorted_names.txt", "r", encoding='utf-8') as file:
    result = []
    for i in file:
        if i == '\n':
            continue
        else:
            result.append(str(i).strip('\n'))
    result_new = sorted(result)

with open("sorted_names.txt", "w", encoding='utf-8') as file:
    for i in result_new:
        file.write(i + '\n')
