"""Скрипт решения домашнего задания №2 из лекции №13"""

from typing import List


class MySquareIterator:

    def __init__(self, lst: List[int]):
        self.lst = lst

    def __next__(self):
        if len(self.lst) > 0:
            return self.lst.pop(0) ** 2
        else:
            raise StopIteration

    def __iter__(self):
        return self


lst = [i for i in range(1, 6)]

##lst = [1, 2, 3, 4, 5]

itr = MySquareIterator(lst)
for el in itr:
    print(el, end=" ")
