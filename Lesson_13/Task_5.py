"""Скрипт решения домашнего задания №5 из лекции №13"""


def endless_fib_generator():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


gen = endless_fib_generator()

##print (gen)
i = 1  # Добавил счетчик, чтобы не зависал компьютер

while True:
    print(next(gen), end=" ")

    i += 1  # Добавил счетчик, чтобы не зависал компьютер
    if i == 100: break  # Добавил счетчик, чтобы не зависал компьютер
