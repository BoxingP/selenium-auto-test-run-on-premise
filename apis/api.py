import os
import urllib.request
import json


class API(object):
    def __init__(self, name):
        self.config = None
        self.load_config(name)

    def load_config(self, name):
        try:
            with open(os.path.join(os.path.dirname(__file__), 'api.json'), 'r', encoding='UTF-8') as file:
                config = json.load(file)
            self.config = [db for db in config if db['name'] == name][0]
        except IndexError as error:
            print(f"Cannot load related {name} API config: {error}.")
            self.config = None

    def send_request(self, url, headers):
        try:
            req = urllib.request.Request(url=url, headers=headers)
            resp = urllib.request.urlopen(req)
            resp = resp.read().decode()
            if resp != '':
                data = json.loads(resp)
                return data
        except Exception as error:
            print(f"Error: {str(error)}")
        return None
