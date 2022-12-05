"""Скрипт решения домашнего задания №3 из лекции №12"""


class InvalidIntDivision(Exception):
    """Ошибка ввода целого числа"""
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"InvalidIntDivision → {self.a} # не делится на 8"


class InvalidIntNumberCount(Exception):
    """Ошибка ввода целого числа"""
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"InvalidIntNumberCount → {self.a} # больше 4 символов"


class InvalidFloat(Exception):
    """Ошибка ввода числа с запятой"""
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"InvalidFloat → {self.a} # больше 2 символов после запятой"


class InvalidTextLength(Exception):
    """Ошибка ввода текста"""
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"InvalidTextLength → {self.a} # больше 4 символов"


class DuplicatesInText(Exception):
    """Ошибка ввода текста"""
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"InvalidTextLength → {self.a} # повторяющиеся символы"




class Queue:
    """Класс очереди"""
    queue = []


    @classmethod
    def test_int(cls, i):
        """Тестирование целых чисел"""
        if i % 8 != 0:
            print (InvalidIntDivision (f"{i}"))
        elif len(str(i)) > 4:
            print (InvalidIntNumberCount (f"{i}"))
        else:
            cls.queue.append(i)


    @classmethod
    def test_float(cls, i):
        """Тестирование чисел с запятой"""
        if len(str(i)[(str(i).find(".") + 1): ]) > 2:
            print (InvalidFloat (f"{i}"))
        else:
            cls.queue.append(i)


    @classmethod
    def test_str(cls, i):
        """Тестирование строк"""
        if len(i) > 4:
            print (InvalidTextLength (f"{i}"))
        elif len([j for j in range(len(i)) if j != i.find(i[j])]):
            print (DuplicatesInText (f"{i}"))
        else:
            cls.queue.append(i)


    @classmethod
    def add(cls, *tup):
        """Функция добавления элементов в очередь"""
        for i in tup:
            if isinstance(i, int):
                cls.test_int(i)
            elif isinstance(i, float):
                cls.test_float(i)
            elif isinstance(i, str):
                cls.test_str(i)
        return cls.queue


Queue.add(1, 16, 280, 80000, 2.51, 1.875, "text", "data", "world", "new")


print(Queue.queue)
