import json

from decouple import config


class User(object):
    def __init__(self):
        self.users = config('USERS', cast=lambda x: json.loads(x))

    def get_user(self, name):
        try:
            return next(user for user in self.users if user['name'] == name)
        except StopIteration:
            print('\n User %s is not defined, enter a valid user.\n' % name)
