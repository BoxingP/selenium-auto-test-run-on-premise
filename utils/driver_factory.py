from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory(object):
    CHROME_OPTIONS = [
        '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"'
    ]
    FIREFOX_OPTIONS = [
        '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"'
    ]
    EDGE_OPTIONS = [
        '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54"'
    ]
    COMMON_OPTIONS = [
        '--window-size=1920,1280',
        '--start-maximized'
    ]
    HEADLESS_OPTIONS = [
        '--headless',
        '--no-sandbox',
        '--disable-gpu',
        '--hide-scrollbars',
        '--single-process',
        '--disable-dev-shm-usage'
    ]

    @staticmethod
    def get_driver(browser, headless_mode=False):
        options = None
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            for option in DriverFactory.CHROME_OPTIONS:
                options.add_argument(option)
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            for option in DriverFactory.FIREFOX_OPTIONS:
                options.add_argument(option)
        elif browser == 'edge':
            options = webdriver.EdgeOptions()
            for option in DriverFactory.EDGE_OPTIONS:
                options.add_argument(option)
        for option in DriverFactory.COMMON_OPTIONS:
            options.add_argument(option)
        if headless_mode:
            for option in DriverFactory.HEADLESS_OPTIONS:
                options.add_argument(option)

        driver = None
        if browser == 'chrome':
            driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=options)
        elif browser == 'firefox':
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        elif browser == 'edge':
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

        if driver is None:
            raise Exception('Provide valid driver name')
        return driver
