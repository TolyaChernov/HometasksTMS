import re


class Validator:
    """A"""

    def validate(self, *args: str):
        self.data = args

        if (
            self.validate_login(self.data[0])
            and self.validate_password(self.data[1])
            and self.validate_email(self.data[2])
        ):
            return True
        else:
            return False

    def validate_login(self, s):

        pattern = r"[a-zA-Z0-9]{6,}$"
        if re.match(pattern, s) is not None:
            return True
        else:
            return False

    def validate_password(self, s):

        pattern = (
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        )
        if re.match(pattern, s) is not None:
            return True
        else:
            return False

    def validate_email(self, s):

        pattern = "^[-\\w\\.]+@[-\\w]+\\.+[-\\w]{2,}$"
        if re.match(pattern, s) is not None:
            return True
        else:
            return False


validator = Validator()
# print(validator.validate("Awqwe1q", "Some!Passwo5rd", "mail@mailc.by"))


# a, b, c = "Awqwe1q", "Some!Passwo5rd", "mail@mailc.by"


# print(validator.validate(a, b, c))
