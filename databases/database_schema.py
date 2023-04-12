import datetime

from sqlalchemy import Column, Integer, String, Time, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class StatusOfFailure(Base):
    __tablename__ = 'status_of_failure'
    id = Column(Integer, primary_key=True, nullable=False)
    case_id = Column(String, nullable=True)
    time = Column(Time, default=datetime.datetime.utcnow(), nullable=False)
    status = Column(Integer, nullable=True)
    sync_platform = Column(String, nullable=True)
    case_id_on_platform = Column(String, nullable=True)
    last_run_id_on_platform = Column(String, nullable=True)


class SeleniumTestSteps(Base):
    __tablename__ = 'selenium_test_steps'
    id = Column(Integer, primary_key=True, nullable=False)
    case_id = Column(String, nullable=False)
    steps = Column(String, nullable=False)
    time = Column(Time, default=datetime.datetime.utcnow(), nullable=False)
    duration = Column(Float, nullable=False)
    status_id = Column(Integer, ForeignKey('status_of_failure.id'))


class SeleniumTestAvailability(Base):
    __tablename__ = 'selenium_test_availability'
    id = Column(Integer, primary_key=True, nullable=False)
    case_id = Column(String, nullable=False)
    time = Column(Time, default=datetime.datetime.utcnow(), nullable=False)
    availability = Column(Integer, nullable=False)


class E1OrderHeader(Base):
    __tablename__ = "F4201"
    __table_args__ = {"schema": "PRODDTA"}
    SHDOCO = Column(Integer, primary_key=True, nullable=False)
    SHDCTO = Column(String, primary_key=True, nullable=False)
    SHKCOO = Column(String, primary_key=True, nullable=False)
    SHTKBY = Column(String, nullable=True)
    SHURCD = Column(String, nullable=True)
    SHTRDJ = Column(Integer, nullable=True)
    SHUPMJ = Column(Integer, nullable=True)
    SHTDAY = Column(Integer, nullable=True)