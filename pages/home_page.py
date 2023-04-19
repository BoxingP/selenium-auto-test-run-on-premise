import allure

from pages.page import Page
from utils.locators import HomePageLocators, LoginPageLocators
from utils.logger import _step


class HomePage(Page):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.locator = HomePageLocators

    @_step
    @allure.step('Open login page')
    def go_to_login_page(self):
        self.click(*self.locator.sign_in_menu)
        self.click(*self.locator.sign_in_button)
        self.wait_url_changed_to('proxy.html')
        self.wait_url_changed_to('signin-identifier.html')
        self.wait_element_to_be_visible(*LoginPageLocators.username_field)
