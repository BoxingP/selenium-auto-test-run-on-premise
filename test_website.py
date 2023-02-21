import json
import os
import shutil

import pytest

from utils.database import Database


def empty_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


def upload_result_to_db(results_file, logs_file):
    results_database = Database()
    with open(results_file, 'r', encoding='UTF-8') as file:
        results = json.load(file)
    tests_results = results['report']['tests']
    for test in tests_results:
        if test['outcome'] == 'passed':
            status = 0
        else:
            status = 1
        status_id = results_database.insert_status('ccp_login_test', status)
        results_database.insert_steps('ccp_login_test', status_id, logs_file)
        results_database.insert_availability('ccp_login_test')


def lambda_handler(event, context):
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r', encoding='UTF-8') as file:
        config = json.load(file)
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    output_dir = os.path.join(os.path.abspath(os.sep), config['output_dir'])
    allure_results_dir = os.path.join(output_dir, config['allure_results_dir'])
    logs_dir = os.path.join(output_dir, config['logs_dir'])
    steps_log_file = os.path.join(logs_dir, 'steps.log')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    json_report_file = os.path.join(output_dir, 'report.json')

    pytest.main(
        [tests_dir, "--dist=loadfile", "--order-dependencies", f"--alluredir={allure_results_dir}", '--cache-clear',
         f"--json={json_report_file}", '-n', '5']
    )
    upload_result_to_db(json_report_file, steps_log_file)
    empty_directory(directory=logs_dir)


if __name__ == '__main__':
    lambda_handler(None, None)
