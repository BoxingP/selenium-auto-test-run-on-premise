import json
import os

import pytest

from utils.database import Database


def upload_availability_to_db():
    results_database = Database()
    results_database.insert_availability('ccp_login_test')


def upload_status_to_db(results_file):
    results_database = Database()
    with open(results_file, 'r', encoding='UTF-8') as file:
        results = json.load(file)
    tests_results = results['report']['tests']
    for test in tests_results:
        if test['outcome'] == 'passed':
            status = 0
        else:
            status = 1
        results_database.insert_status('ccp_login_test', status)


def lambda_handler(event, context):
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r', encoding='UTF-8') as file:
        config = json.load(file)
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    tmp_dir = os.path.join(os.path.abspath(os.sep), 'tmp')
    allure_results_dir = os.path.join(tmp_dir, config['allure_results_dir'])
    logs_dir = os.path.join(tmp_dir, config['logs_dir'])
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    json_report_file = os.path.join(tmp_dir, 'report.json')

    pytest.main(
        [tests_dir, "--dist=loadfile", "--order-dependencies", f"--alluredir={allure_results_dir}", '--cache-clear',
         f"--json={json_report_file}", '-n', '5']
    )
    upload_status_to_db(json_report_file)
    upload_availability_to_db()


if __name__ == '__main__':
    lambda_handler(None, None)
