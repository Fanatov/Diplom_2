import random
import string


class GeneratedPayloads:
    def __init__(self):
        self.RANDOM_PAYLOAD = {
            "email": self.create_random_mail(),
            "password": self.create_random_password(),
            "name": self.create_random_name()
        }
        self.MAIL_PASS_ONLY = {"email": self.create_random_mail(),
                          "password": self.create_random_password()}

        self.MAIL_ONLY = {"email": self.create_random_mail()}
        self.PASSWORD_ONLY = {"password": self.create_random_password()}
        self.NAME_ONLY = {"name": self.create_random_name()}

    def create_random_mail(self):
        name = ''.join(random.choices(string.ascii_letters, k=12))
        random_digits = str(random.randint(1, 1999))
        result_login = name + random_digits + '@ya.ru'
        return result_login

    def create_random_password(self):
        password = ''.join(random.choices(string.ascii_letters, k=8))
        random_digits = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        result_password = f'{password}{random_digits}'
        return result_password

    def create_random_name(self):
        name = ''.join(random.choices(string.ascii_letters, k=7))
        random_digits = str(random.randint(1, 1999))
        result_name = name + random_digits
        return result_name
