import json
import os
from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()


class Database(object):
    def __init__(self, name):
        with open(os.path.join(os.path.dirname(__file__), 'db.json'), 'r', encoding='UTF-8') as file:
            config = json.load(file)
        self.db_config = [db for db in config if db['name'] == name][0]
        engine = self.create_engine()
        Session.configure(bind=engine)
        self.session = Session()

    def create_engine(self):
        adapter = self.db_config['adapter']
        host = self.db_config['host']
        port = self.db_config['port']
        database = self.db_config['database']
        user = self.db_config['user']
        password = self.db_config['password']
        db_uri = f'{adapter}://{user}:%s@{host}:{port}/{database}' % quote(password)
        return create_engine(db_uri, echo=False)
