import json
import os
import shutil
import subprocess

import pytest


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


def move_files_from_directory_to_another(source, target):
    if os.path.exists(source):
        files = os.listdir(source)
        if not os.path.exists(target):
            os.makedirs(target)
        for file in files:
            shutil.move(os.path.join(source, file), os.path.join(target, file))


def generate_allure_reports(result_path, report_path):
    if os.path.exists(report_path):
        history_path = os.path.join(report_path, 'history')
        if os.path.exists(history_path):
            move_files_from_directory_to_another(history_path, os.path.join(result_path, 'history'))
    else:
        os.makedirs(report_path)
    subprocess.call(['powershell', '-command', f'allure generate -c {result_path} -o {report_path}'])
    empty_directory(result_path)


def generate_env_properties(target_path, config):
    with open(os.path.join(target_path, 'environment.properties'), 'w', encoding='UTF-8') as file:
        line1 = f"Browser={config['browser']}\n"
        line2 = f"BrowserVersion={config['browser_version']}\n"
        line3 = f"Environment={config['environment']}\n"
        line4 = f"Python={config['python']}\n"
        line5 = f"MonitoredSite={config['base_url']}"
        file.writelines([line1, line2, line3, line4, line5])


def lambda_handler(event, context):
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r', encoding='UTF-8') as file:
        config = json.load(file)
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    tmp_dir = os.path.join(os.path.abspath(os.sep), 'tmp')
    allure_results_dir = os.path.join(tmp_dir, config['allure_results_dir'])
    allure_reports_dir = os.path.join(tmp_dir, config['allure_reports_dir'])
    logs_dir = os.path.join(tmp_dir, config['logs_dir'])
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    pytest.main(
        [tests_dir, "--dist=loadfile", "--order-dependencies", f"--alluredir={allure_results_dir}", '--cache-clear',
         '-n', '5']
    )
    generate_env_properties(allure_results_dir, config)
    generate_allure_reports(allure_results_dir, allure_reports_dir)


if __name__ == '__main__':
    lambda_handler(None, None)
