import allure

from pages.page import Page
from utils.locators import RequestQuotePageLocators
from utils.logger import _step


class RequestQuotePage(Page):
    def __init__(self, driver):
        super(RequestQuotePage, self).__init__(driver)
        self.locator = RequestQuotePageLocators

    @_step
    @allure.step('Wait for request form to be visible on page')
    def wait_request_form_visible(self):
        self.wait_element_to_be_invisible(*self.locator.loading_circle)
        self.wait_frame_to_be_visible(*self.locator.request_quote_iframe)
        self.scroll_page(direction='down')
        self.wait_element_to_be_visible(*self.locator.comments_input_box)
        self.wait_element_to_be_clickable(*self.locator.submit_button)
