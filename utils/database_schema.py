import datetime

from sqlalchemy import Column, Integer, String, Time, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SeleniumTestStatus(Base):
    __tablename__ = 'selenium_test_status'
    id = Column(Integer, primary_key=True, nullable=False)
    case_id = Column(String, nullable=False)
    time = Column(Time, default=datetime.datetime.utcnow(), nullable=False)
    status = Column(Integer, default='System', nullable=False)


class SeleniumTestSteps(Base):
    __tablename__ = 'selenium_test_steps'
    id = Column(Integer, primary_key=True, nullable=False)
    case_id = Column(String, nullable=False)
    steps = Column(String, nullable=False)
    time = Column(Time, default=datetime.datetime.utcnow(), nullable=False)
    duration = Column(Float, nullable=False)
    status_id = Column(Integer, ForeignKey('selenium_test_status.id'))


class SeleniumTestAvailability(Base):
    __tablename__ = 'selenium_test_availability'
    id = Column(Integer, primary_key=True, nullable=False)
    case_id = Column(String, nullable=False)
    time = Column(Time, default=datetime.datetime.utcnow(), nullable=False)
    availability = Column(Integer, nullable=False)
