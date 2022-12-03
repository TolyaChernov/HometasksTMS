"""Модуль позволяет кодировать и декодировать заданную строку"""


class Cipher:

    def __init__(self):
        """Инициализирует переменные"""
        self.encod = None
        self.dencod = None
        self.s_output_e = ''
        self.s_output_d = ''
        self.text_inp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.text_key = ['C', 'R', 'Y', 'P', 'T', 'O', 'A', 'B', 'D', 'E',
                         'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                         'Q', 'S', 'U', 'V', 'W', 'X', 'Z']

    def encode(self, encod):
        """Кодирование заданной строки"""
        self.encod = encod
        for i in self.encod:
            try:  # Перенос символов, которых нет в "ключе", в результат
                ind = self.text_inp.index(i.upper())
            except ValueError:
                self.s_output_e += i
                continue
            if i.isupper():
                self.s_output_e += self.text_key[ind]
            else:
                self.s_output_e += self.text_key[ind].lower()

        print(self.s_output_e)

    def decode(self, dencod):
        """Декодирование заданной строки"""
        self.dencod = dencod
        for i in self.dencod:
            try:  # Перенос символов, которых нет в "ключе", в результат
                ind = self.text_key.index(i.upper())
            except ValueError:
                self.s_output_d += i
                continue
            if i.isupper():
                self.s_output_d += self.text_inp[ind]
            else:
                self.s_output_d += self.text_inp[ind].lower()

        print(self.s_output_d)


cipher = Cipher()

cipher.encode("Hello world!!!")
cipher.decode("Fjedhc dn atidsn №1")

