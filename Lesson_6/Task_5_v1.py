#!/bin/bash
# !/usr/bin/python3


def combine_dicts(*args):
    dict_res = dict()
    for i in args:
        for key, value in i.items():
            if key in dict_res.keys():
                dict_res[key] = value + dict_res[key]
            else:
                dict_res[key] = value

    #    print("Результат сложения: ", dict_res)
    return dict_res


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
