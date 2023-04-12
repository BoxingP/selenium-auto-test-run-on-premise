import datetime

from sqlalchemy import select

from databases.database import Database
from databases.database_schema import StatusOfFailure, SeleniumTestSteps, SeleniumTestAvailability
from utils.steps_log import StepsLog


class OpsDatabase(Database):
    def __init__(self, name):
        super(OpsDatabase, self).__init__(name)

    def insert_status(self, name, status):
        new_status = StatusOfFailure(
            case_id=name,
            status=status,
            sync_platform='Selenium'
        )
        self.session.add(new_status)
        self.session.flush()
        self.session.commit()
        return new_status.id

    def insert_steps(self, case, status_id, steps):
        with open(steps) as file:
            logs = file.read()
        if logs != '':
            for line in logs.split('\n'):
                if line == '':
                    continue
                log = StepsLog(line)
                if case['test_name'].replace('_', ' ') != log.test:
                    continue
                step = SeleniumTestSteps(
                    case_id=case['case_name'],
                    steps=log.step,
                    time=log.log_dt,
                    duration=log.spent_time,
                    status_id=status_id
                )
                self.session.add(step)
                self.session.commit()

    def insert_availability(self, name, hours: int = -2):
        total_statement = select(StatusOfFailure.time, StatusOfFailure.status).filter(
            StatusOfFailure.time >= datetime.datetime.utcnow() + datetime.timedelta(hours=hours)).filter_by(
            case_id=name)
        rows = self.session.execute(total_statement).all()
        total_status = len(rows)
        passed_statement = total_statement.filter_by(status=0)
        rows = self.session.execute(passed_statement).all()
        passed_status = len(rows)
        availability = round(passed_status / total_status * 100)
        new_availability = SeleniumTestAvailability(
            case_id=name,
            availability=availability
        )
        self.session.add(new_availability)
        self.session.commit()
