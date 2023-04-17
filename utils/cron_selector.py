import datetime

import pytz
from apscheduler.triggers.cron import CronTrigger


def match(cron: str, current_time=None):
    if not current_time:
        utc_now = datetime.datetime.utcnow().replace(second=0, microsecond=0)
        china_tz = pytz.timezone('Asia/Shanghai')
        current_time = utc_now.replace(tzinfo=pytz.utc).astimezone(china_tz)
    trigger = CronTrigger.from_crontab(cron)
    if trigger.get_next_fire_time(None, current_time) == current_time:
        return True
    else:
        return False


def get_test_cases_to_run(test_cases: list):
    result = []
    for test_case in test_cases:
        if match(test_case['cron']):
            result.append(test_case['test_name'])
    return result
