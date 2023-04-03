from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory(object):

    @staticmethod
    def get_driver(browser, headless_mode=False):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--window-size=1920,1280')
            options.add_argument('--start-maximized')
            if headless_mode is True:
                options.add_argument('--headless')
                options.add_argument('--disable-infobars')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--hide-scrollbars')
                options.add_argument('--single-process')
                options.add_argument('--ignore-certificate-errors')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument(
                    '--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36""')
            driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=options)
            return driver
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--window-size=1920,1280')
            options.add_argument('--start-maximized')
            if headless_mode is True:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--ignore-certificate-errors')
                options.add_argument('--allow-running-insecure-content')
                options.add_argument('--disable-extensions')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument(
                    '--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0""')
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            return driver
        elif browser == 'edge':
            options = webdriver.EdgeOptions()
            options.add_argument('--window-size=1920,1280')
            options.add_argument('--start-maximized')
            if headless_mode is True:
                options.add_argument('--headless=new')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--ignore-certificate-errors')
                options.add_argument('--allow-running-insecure-content')
                options.add_argument('--disable-extensions')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument(
                    '--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54""')
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
            return driver

        raise Exception('Provide valid driver name')
