"""Скрипт решения домашнего задания №2 из лекции №12"""


class InvalidLogin(Exception):
    """Ошибка ввода чисел"""

class InvalidPassword(Exception):
    """Ошибка ввода формулы"""

class InvalidEmail(Exception):
    """Ошибка ввода оператора"""

class ValidationError(Exception):
    """Ошибка валидации"""


class Validator:
    """Класс Validator"""



    def validate(self, *args):
        """Инициализация"""
        self.data = args
        try:
            self.validate_login()
            self.validate_password(self.data[1])
            self.validate_email(self.data[2])
        except (InvalidLogin, InvalidPassword, InvalidEmail):
            raise ValidationError
        return True

    def validate_login(self):
        """Проверка логина"""
        if len(self.data[0]) < 6:
            raise InvalidLogin("Количество символов меньше 6")

    def validate_password(self, s):
        """Проверка пароля"""
        if len(self.data[0]) < 8:
            raise InvalidPassword("Не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа")
        elif len([i for i in s if i.isupper()]) < 1:
            raise InvalidPassword("Не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа")
        elif len([i for i in s if i.islower()]) < 1:
            raise InvalidPassword("Не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа")
        elif len([i for i in s if i.isdecimal()]) < 1:
            raise InvalidPassword("Не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа")
        elif set(".,:;?№%:?*!_*-+()/#¤%&)").isdisjoint(s):
            raise InvalidPassword("Не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа")



    def validate_email(self, s):
        """Проверка имаила"""
        if "@" not in s:
            raise InvalidEmail()
        elif "." != s[-3]:
            raise InvalidEmail()
        elif not s[-2:].isalpha():
            raise InvalidEmail()




validator = Validator()
print(validator.validate("user_login", "Some!Passwo5rd", "mail@mail.c.om"))
