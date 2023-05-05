import json
import os
import sys

from decouple import config as decouple_config


class Config(object):
    OUTPUT_ROOT_DIR = os.path.join(os.path.abspath(os.sep), decouple_config('ROOT_DIR', default='tmp'))
    ALLURE_RESULTS_DIR = os.path.join(OUTPUT_ROOT_DIR, decouple_config('ALLURE_RESULTS_DIR', default='allure-results'))
    LOGS_DIR = os.path.join(OUTPUT_ROOT_DIR, decouple_config('LOGS_DIR', default='logs'))
    SCREENSHOTS_DIR = os.path.join(OUTPUT_ROOT_DIR, decouple_config('SCREENSHOTS_DIR', default='screenshots'))
    os.environ['SCREENSHOTS_DIR'] = SCREENSHOTS_DIR
    for directory in [OUTPUT_ROOT_DIR, ALLURE_RESULTS_DIR, LOGS_DIR, SCREENSHOTS_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)
    LOG_FILE = os.path.join(LOGS_DIR, decouple_config('LOG_FILE', default='steps.log'))
    os.environ['LOG_FILE_PATH'] = LOG_FILE
    JSON_REPORT_FILE = os.path.join(OUTPUT_ROOT_DIR, decouple_config('JSON_REPORT_FILE', default='report.json'))
    os.environ['PYTHON_VERSION'] = f"{sys.version_info.major}.{sys.version_info.minor}"
    TEST_CASES = decouple_config('TEST_CASES', cast=json.loads, default=[])


config = Config()
