"""Скрипт решения домашнего задания №3 из лекции №11"""


class DataObject:
    data = []

    def append_right(self, param):
        pass


class Deque(DataObject):
    """Класс очереди"""
    deque = [0]  # В очередь добавлен элемент для удобства проверки кода

    j: int = 5  # длина очереди

    def _proc_add(self, i, j, k):
        """Функция добавления элементов в очередь"""
        if len(self.deque) >= j:
            print(f"Очередь переполнена, пожалуйста, освободите очередь, в очереди {len(self.deque)} элементов")
        else:
            return self.deque.insert(k, i)

    def _proc_del(self, i):
        """Функция удаления элементов из очереди"""
        return self.deque.pop(i)

    @classmethod
    def append_left(cls, i):
        """Функция добавления элементов в очередь слвева"""
        _k: int = 0
        cls._proc_add(cls, i, cls.j, _k)

    @classmethod
    def append_right(cls, i):
        """Функция добавления элементов в очередь справа"""
        k = cls.j
        cls._proc_add(cls, i, cls.j, k)

    @classmethod
    def pop_right(cls):
        """Функция удаления элементов из очереди справа"""
        i = len(cls.deque) - 1
        cls._proc_del(cls, i)

    @classmethod
    def pop_left(cls):
        """Функция удаления элементов из очереди слева"""
        i: int = 0
        cls._proc_del(cls, i)


class TestClass:
    """Класс для тестирования добавления только экземпляров класса DataObject (и его дочерних)"""
    pass


obj_1 = TestClass()
obj_1.append_right(7) if isinstance(obj_1, DataObject) else print("Экземпляр класс не принадлежит классу DataObject")

obj = Deque()

obj.append_right(1) if isinstance(obj, DataObject) else print("Экземпляр класс не принадлежит классу DataObject")
print(Deque.deque)

obj.append_left(2) if isinstance(obj, DataObject) else print("Экземпляр класс не принадлежит классу DataObject")
print(Deque.deque)

obj.append_right(3) if isinstance(obj, DataObject) else print("Экземпляр класс не принадлежит классу DataObject")
print(Deque.deque)

obj.append_left(4) if isinstance(obj, DataObject) else print("Экземпляр класс не принадлежит классу DataObject")
print(Deque.deque)

obj.append_right(5) if isinstance(obj, DataObject) else print("Экземпляр класс не принадлежит классу DataObject")
print(Deque.deque)

obj.append_left(6) if isinstance(obj, DataObject) else print("Экземпляр класс не принадлежит классу DataObject")
print(Deque.deque)

Deque.pop_right()
print(Deque.deque)

Deque.pop_right()
print(Deque.deque)

Deque.pop_left()
print(Deque.deque)

