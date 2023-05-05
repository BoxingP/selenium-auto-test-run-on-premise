import json
import os
import re
import shutil

from databases.ops_database import OpsDatabase
from emails.emails import Emails


def get_screenshot_path(test_name, screenshots_dir):
    screenshots = os.listdir(screenshots_dir)
    test_name = test_name.replace('[', '\\[').replace(']', '\\]')
    pattern = re.compile(test_name, re.IGNORECASE)
    related_screenshots = [file for file in screenshots if pattern.search(file)]
    if related_screenshots:
        related_screenshots.sort(key=lambda f: int(re.sub('[^0-9]', '', f)))
        return os.path.join(screenshots_dir, related_screenshots[-1])
    return ''


def get_failed_tests(json_data: json, test_cases, directory: str):
    failed_tests = []
    for test in json_data['report']['tests']:
        if test['outcome'] in ['passed', 'skipped']:
            continue
        name = test['name'].split("::")[-1]
        stage_outcome = []
        stage_detail = []
        for key in ('name', 'duration', 'run_index', 'outcome'):
            test.pop(key, None)
        for stage in test.values():
            if stage['outcome'] in ['passed', 'skipped']:
                continue
            stage_outcome.append(f"{stage['name']} {stage['outcome']}")
            detail = ''
            for key in [key for key in list(stage.keys()) if key not in ('name', 'duration', 'outcome')]:
                detail = f'{detail}\n    {stage[key]}'
            stage_detail.append(f"\n  {stage['name']}: {detail}")

        summary = ', '.join(stage_outcome)
        screenshot_path = ''
        if 'call' in summary:
            screenshot_path = get_screenshot_path(test_name=name, screenshots_dir=directory)
        detail = '  '.join(stage_detail)
        case = get_test_case(test_cases, name.split("[")[0])
        failed_tests.append(
            {'name': case['case_name'], 'reason': summary, 'screenshot': screenshot_path, 'error': detail})

    return failed_tests


def send_notification(results_file, test_cases, screenshots_dir):
    with open(results_file, 'r', encoding='UTF-8') as file:
        results = json.load(file)
    failed_tests = get_failed_tests(results, test_cases, screenshots_dir)
    if failed_tests:
        Emails().send_email(failed_tests)


def get_test_case(cases, name):
    try:
        return next(case for case in cases if case['test_name'] == name)
    except StopIteration:
        print(f'\n Case {name} is not defined, enter a valid case.\n')


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
    results_database = OpsDatabase('OPS_ALERT')
    with open(results_file, 'r', encoding='UTF-8') as file:
        results = json.load(file)
    tests_results = results['report']['tests']
    for test in tests_results:
        if test['outcome'] == 'passed':
            status = 0
        else:
            status = 1
        case = get_test_case(test_cases, test['name'].split('::')[-1].split("[")[0])
        status_id = results_database.insert_status(case['case_name'], status)
        results_database.insert_steps(case, status_id, logs_file)
        results_database.insert_availability(case['case_name'])
