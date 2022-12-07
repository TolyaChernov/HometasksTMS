"""Скрипт решения домашнего задания №4 из лекции №13"""


class EvenRange:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.it = start

    def __next__(self):
        if self.it < self.end - 1:
            if self.it % 2 == 0:
                res = self.it
                self.it += 2
                return res
            else:
                self.it += 1
                res = self.it
                self.it += 1
                return res
        else:
            print("Out of numbers!")
            exit()

    def __iter__(self):
        return self


er2 = EvenRange(3, 14)

for number in er2:
    print(number, end=" ")

##er1 = EvenRange(7,11)
##
##print(next(er1))
##print(next(er1))
##print(next(er1))
##print(next(er1))
##print(next(er1))
