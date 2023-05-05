import os

import pytest

from utils.config import config
from utils.cron_selector import get_test_cases_to_run
from utils.random_generator import random_browser, random_sleep
from utils.utils import upload_result_to_db, send_notification, empty_directory


def main():
    test_cases_to_run = get_test_cases_to_run(config.TEST_CASES)
    print(f"Running tests: {', '.join(test_cases_to_run)}")
    if test_cases_to_run:
        random_browser()
        random_sleep()
        pytest.main(
            [f"{os.path.join(os.path.dirname(__file__), 'tests')}", "--dist=loadfile", "--order-dependencies",
             f"--alluredir={config.ALLURE_RESULTS_DIR}", '--cache-clear',
             f"--json={config.JSON_REPORT_FILE}", '-n', '5', '-k', ' or '.join(test_cases_to_run)]
        )
        upload_result_to_db(config.JSON_REPORT_FILE, config.LOG_FILE, config.TEST_CASES)
        send_notification(config.JSON_REPORT_FILE, config.TEST_CASES, config.SCREENSHOTS_DIR)
        empty_directory(directory=config.LOGS_DIR)
        empty_directory(directory=config.SCREENSHOTS_DIR)


if __name__ == '__main__':
    main()
