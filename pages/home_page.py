import allure

from pages.page import Page
from utils.locators import HomePageLocators, LoginPageLocators
from utils.logger import _step


class HomePage(Page):
    def __init__(self, driver, config):
        super(HomePage, self).__init__(driver, config)
        self.locator = HomePageLocators

    @_step
    @allure.step('Redirect to login page')
    def redirect_to_login(self):
        self.wait_url_changed_to('signin-identifier.html')
        self.wait_element_to_be_visible(*LoginPageLocators.username_field)

    @_step
    def search_org(self, name):
        self.input_text(name, *self.locator.search_org_field)
        self.click(*self.locator.search_org_button)
        self.wait_element_to_be_visible(*self.locator.search_org_result)

    @_step
    def open_org_dashboard(self):
        self.hover(*self.locator.search_org_result)
        self.click(*self.locator.dashboard_button)
        self.wait_url_changed_to('dashboard')

    @_step
    def open_instrument_group_dashboard(self):
        self.click(*self.locator.instrument_group)
        self.wait_url_changed_to('group')
        self.wait_element_to_be_invisible(*self.locator.group_consumable_state_table_loading)
        self.wait_element_to_be_visible(*self.locator.group_consumable_state_table)
