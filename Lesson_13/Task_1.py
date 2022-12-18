"""Скрипт решения домашнего задания №1 из лекции №13"""


def names_gen(path, letter: str):
    with open(path, "r") as file:
        for line in file:
            if line.startswith(letter):
                yield line



names_with_letter = names_gen("unsorted_names.txt", "A")

for name in names_with_letter:
    print(name, end="")
