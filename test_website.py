import json
import os
import shutil

import pytest

from utils.database import Database


def get_test_case(cases, name):
    try:
        return next(case for case in cases if case['test_name'] == name)
    except StopIteration:
        print('\n Case %s is not defined, enter a valid case.\n' % name)


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


def upload_result_to_db(results_file, logs_file, test_cases):
    results_database = Database()
    with open(results_file, 'r', encoding='UTF-8') as file:
        results = json.load(file)
    tests_results = results['report']['tests']
    for test in tests_results:
        if test['outcome'] == 'passed':
            status = 0
        else:
            status = 1
        case = get_test_case(test_cases, test['name'].split('::')[-1])
        status_id = results_database.insert_status(case['case_name'], status)
        results_database.insert_steps(case['case_name'], status_id, logs_file)
        results_database.insert_availability(case['case_name'])


def lambda_handler(event, context):
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r', encoding='UTF-8') as file:
        config = json.load(file)
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    output_dir = os.path.join(os.path.abspath(os.sep), config['output_dir'])
    allure_results_dir = os.path.join(output_dir, config['allure_results_dir'])
    logs_dir = os.path.join(output_dir, config['logs_dir'])
    steps_log_file = os.path.join(logs_dir, 'steps.log')
    utils_dir = os.path.join(os.path.dirname(__file__), 'utils')
    with open(os.path.join(utils_dir, 'logging_config_template.json'), 'r', encoding='UTF-8') as file:
        logging_config = json.load(file)
    logging_config['handlers']['info_file']['filename'] = steps_log_file
    with open(os.path.join(utils_dir, 'logging_config.json'), 'w') as file:
        json.dump(logging_config, file)
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    json_report_file = os.path.join(output_dir, 'report.json')

    pytest.main(
        [tests_dir, "--dist=loadfile", "--order-dependencies", f"--alluredir={allure_results_dir}", '--cache-clear',
         f"--json={json_report_file}", '-n', '5']
    )
    upload_result_to_db(json_report_file, steps_log_file, config['test_cases'])
    empty_directory(directory=logs_dir)


if __name__ == '__main__':
    lambda_handler(None, None)
