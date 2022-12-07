"""Скрипт решения домашнего задания №2 из лекции №13"""

import re


class Validator:
    """A"""

    def validate(self, *args: str):
        self.data = args

        if self.validate_login(self.data[0]) == True and self.validate_password(
                self.data[1]) == True and self.validate_email(self.data[2]) == True:
            return True
        else:
            return False

    def validate_login(self, s):

        pattern = r'[a-zA-Z0-9-_\.]{5,10}$'
        if re.match(pattern, s) is not None:
            return True
        else:
            return False

    def validate_password(self, s):

        pattern = r'[A-Za-z0-9@#$%^&+=!]{8,}'
        if re.match(pattern, s) is not None:
            return True
        else:
            return False

    def validate_email(self, s):

        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2}$"
        if re.match(pattern, s) is not None:
            return True
        else:
            return False


validator = Validator()
print(validator.validate("Awqwe1q", "Some!Passwo5rd", "mail@mailc.by"))
