import allure

from pages.page import Page
from utils.locators import LoginPageLocators
from utils.logger import _step
from utils.users import User


class LoginPage(Page):
    def __init__(self, driver, config):
        super(LoginPage, self).__init__(driver, config)
        self.locator = LoginPageLocators

    @_step
    @allure.step('Login with user: {user}')
    def login(self, user, is_valid):
        user = User().get_user(user)
        self.input_text(user['email'], *self.locator.username_field)
        self.click(*self.locator.next_button)
        self.input_text(user['password'], *self.locator.password_field)
        self.click(*self.locator.sign_in_button)
        if not is_valid:
            self.wait_element(*self.locator.login_error_notice)

    @_step
    @allure.step('Redirect to home page')
    def redirect_to_home(self):
        self.wait_url_changed_to('proxy.html')
        self.wait_url_changed_to('msd-cp')
