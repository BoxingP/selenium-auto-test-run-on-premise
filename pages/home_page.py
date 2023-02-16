import allure

from pages.page import Page
from utils.locators import HomePageLocators
from utils.logger import _step


class HomePage(Page):
    def __init__(self, driver, config):
        super(HomePage, self).__init__(driver, config)
        self.locator = HomePageLocators

    @_step
    @allure.step('Redirect to login page')
    def redirect_to_login(self):
        self.wait_url_changed_to('signin-identifier.html')
