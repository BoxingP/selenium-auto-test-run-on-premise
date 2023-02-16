import datetime
import json
import os
from urllib.parse import quote

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from utils.database_schema import CCPTestResults, CCPLoginAvailability

Session = sessionmaker()


class Database(object):
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), 'db.json'), 'r', encoding='UTF-8') as file:
            self.config = json.load(file)
        engine = self.create_engine()
        Session.configure(bind=engine)
        self.session = Session()

    def create_engine(self):
        db_config = self.config['database']
        adapter = db_config['adapter']
        host = db_config['host']
        port = db_config['port']
        database = db_config['database']
        user = db_config['user']
        password = db_config['password']
        db_uri = f'{adapter}://{user}:%s@{host}:{port}/{database}' % quote(password)
        return create_engine(db_uri, echo=False)

    def insert_status(self, name, status):
        new_status = CCPTestResults(
            case_id=name,
            status=status
        )
        self.session.add(new_status)
        self.session.commit()

    def insert_availability(self, name):
        statement = select(CCPTestResults.time, CCPTestResults.status).filter(
            CCPTestResults.time >= datetime.datetime.utcnow() + datetime.timedelta(hours=-2))
        rows = self.session.execute(statement).all()
        total_status = len(rows)
        statement = select(CCPTestResults.time, CCPTestResults.status).filter(
            CCPTestResults.time >= datetime.datetime.utcnow() + datetime.timedelta(hours=-2)).filter_by(status=0)
        rows = self.session.execute(statement).all()
        available_status = len(rows)
        availability = round(available_status / total_status * 100)
        new_availability = CCPLoginAvailability(
            case_id=name,
            availability=availability
        )
        self.session.add(new_availability)
        self.session.commit()
