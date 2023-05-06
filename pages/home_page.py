import allure

from pages.locators import HomePageLocators, LoginPageLocators
from pages.page import Page
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

    @_step
    @allure.step('Check if user already logged in')
    def is_user_logged_in(self):
        return self.is_element_exists(*self.locator.logged_in_menu)

    @_step
    @allure.step('Logout')
    def logout(self):
        self.click(*self.locator.logged_in_menu)
        self.click(*self.locator.sign_out_link)
        self.wait_element_to_be_visible(*self.locator.logo_img)
