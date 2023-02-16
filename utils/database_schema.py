import datetime

from sqlalchemy import Column, Integer, String, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CCPTestResults(Base):
    __tablename__ = 'ccp_test_results'
    id = Column(Integer, primary_key=True, nullable=False)
    case_id = Column(String, nullable=False)
    time = Column(Time, default=datetime.datetime.utcnow(), nullable=False)
    status = Column(Integer, default='System', nullable=False)


class CCPLoginAvailability(Base):
    __tablename__ = "ccp_login_availability"
    id = Column(Integer, primary_key=True, nullable=False)
    case_id = Column(String, nullable=False)
    time = Column(Time, default=datetime.datetime.utcnow(), nullable=False)
    availability = Column(Integer, nullable=False)
