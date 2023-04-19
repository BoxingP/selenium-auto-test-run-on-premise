import datetime
import os

import allure
from allure_commons.types import AttachmentType
from decouple import config


class Screenshot(object):

    @staticmethod
    def take_screenshot(driver, message, test=''):
        if test == '':
            test = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0].lower()
        current = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
        img_name = f'{test}_{current}.png'
        img_dir = config('SCREENSHOTS_DIR_PATH')
        img_path = os.path.join(img_dir, img_name)
        img = driver.get_screenshot_as_file(img_path)
        if not img:
            os.makedirs(img_dir)
            img = driver.get_screenshot_as_file(img_path)
        with open(img_path, mode='rb') as image:
            allure.attach(image.read(), name=message, attachment_type=AttachmentType.PNG)
