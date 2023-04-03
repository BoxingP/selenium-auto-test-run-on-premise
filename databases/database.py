from urllib.parse import quote

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()


class Database(object):
    def __init__(self, name):
        adapter = config(f'{name}_ADAPTER')
        host = config(f'{name}_HOST')
        port = config(f'{name}_PORT')
        database = config(f'{name}_DATABASE')
        user = config(f'{name}_USER')
        password = config(f'{name}_PASSWORD')
        db_uri = f'{adapter}://{user}:%s@{host}:{port}/{database}' % quote(password)
        engine = create_engine(db_uri, echo=False)
        Session.configure(bind=engine)
        self.session = Session()
