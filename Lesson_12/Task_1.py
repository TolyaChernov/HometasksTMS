"""Скрипт решения домашнего задания №1 из лекции №12"""

class InputFormulaError(Exception):
    """Ошибка ввода формулы"""

class InputNumberError(Exception):
    """Ошибка ввода чисел"""

class InputOperatorError(Exception):
    """Ошибка ввода оператора"""


def start():
    """Старт работы"""
    s = input("Ввести выражение: ")
    if s == "quit":
        print("Программа завершена")
        exit()
    else:
        test(s)


def test(s):
    """Тестирование введенных данных"""
    d = s.split(" ")
    if len(d) != 3:
        raise InputFormulaError
    elif not d[0].isdigit() or not d[2].isdigit():
        raise InputNumberError
    elif not d[1] in ["+", "-", "*", "/", "**"]:
        raise InputOperatorError
    play(s)


def play(s):
    """Вычисление"""
    a, o, b = s.split(" ")
    if o == "+":
        print("Ответ: ", int(a) + int(b))
    elif o == "-":
        print("Ответ: ", int(a) - int(b))
    elif o == "*":
        print("Ответ: ", int(a) * int(b))
    elif o == "/":
        print("Ответ: ", int(a) / int(b))
    elif o == "**":
        print("Ответ: ", int(a) ** int(b))
    start()


start()
