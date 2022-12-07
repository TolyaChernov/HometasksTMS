"""Скрипт решения домашнего задания №1 из лекции №13"""


def names_gen(path, letter: str):
    with open(path, "r") as file:
        list_name = (name for name in file if letter in name)
        for i in list_name:
            yield i


names_with_letter = names_gen("unsorted_names.txt", "A")

for name in names_with_letter:
    print(name, end="")
