import datetime
import re


class StepsLog(object):
    def __init__(self, log: str):
        self.test = None
        self.step = None
        self.log_dt = None
        self.spent_time = None
        self.parse_log(log)

    def get_date(self, string):
        date_fmt = r'%Y-%m-%d %H:%M:%S,%f'
        self.log_dt = datetime.datetime.strptime(string, date_fmt)

    def get_details(self, string):
        details = string.rstrip().split('.')
        self.test = details[1].replace('_', ' ')
        self.step = details[2].replace('_', ' ')

    def parse_log(self, log: str):
        part = log.rstrip().split(' - ')
        self.get_date(part[0])
        self.get_details(part[1])
        self.spent_time = float((part[2].rstrip().split(' '))[0])
