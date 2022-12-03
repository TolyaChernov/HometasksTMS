class Counter:
    """Класс счетчика с возможностью
    установления начального
    и конечного значений"""

    def __init__(self, start=None, stop=None):
        """Инициализирует переменные start и stop"""
        self.start = start
        self.stop = stop
        self.current = start

    def increment(self):
        """Увеличивает счетчик на 1"""
        if self.current is None:
            self.current = 0

        if self.stop is None:
            self.current += 1
        else:
            if self.current < self.stop:
                self.current += 1
            else:
                print("Maximal value is reached")
        return self.current

    def get(self):
        """Выводит информацию о значении счетчика"""
        print(self.current)


c = Counter(start=42)
c.increment()
c.get()
# 43

c = Counter()
c.increment()
c.get()
# 1
c.increment()
c.get()
# 2

c = Counter(start=42, stop=43)
c.increment()
c.get()
# 43
c.increment()
# Maximal value is reached.
c.get()
# 43

