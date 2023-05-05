import json

from decouple import config as decouple_config


class User(object):
    def __init__(self):
        self.users = decouple_config('USERS', cast=lambda x: json.loads(x))

    def get_user(self, name):
        try:
            return next(user for user in self.users if user['name'] == name)
        except StopIteration:
            print(f'\n User {name} is not defined, enter a valid user.\n')
