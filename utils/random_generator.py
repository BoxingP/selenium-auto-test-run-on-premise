import os
import random
from time import sleep

from decouple import config


def random_browser():
    browser_list = config('BROWSER', cast=lambda x: x.split(','))
    selected_browser = random.choice(browser_list)
    print(f"Using {selected_browser} to do the test.")
    os.environ['BROWSER'] = selected_browser


def random_sleep():
    start = round(random.random(), 1) * 10
    range_values = tuple(map(int, config('SLEEP_TIME_UPPER_LIMIT_RANGE').strip('()').split(',')))
    stop = random.randint(*range_values)
    seconds = round(random.uniform(start, stop), 5)
    print(f"Random sleeping {seconds} seconds ...")
    sleep(seconds)
