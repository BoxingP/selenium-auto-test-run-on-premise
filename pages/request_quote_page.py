import allure

from pages.locators import RequestQuotePageLocators
from pages.page import Page
from utils.logger import _step


class RequestQuotePage(Page):
    def __init__(self, driver):
        super(RequestQuotePage, self).__init__(driver)
        self.locator = RequestQuotePageLocators

    @_step
    @allure.step('Wait for request form to be visible on page')
    def wait_elms_skus_request_form_visible(self):
        self.wait_element_to_be_invisible(*self.locator.elms_skus_loading_circle)
        self.wait_frame_to_be_visible(*self.locator.elms_skus_request_quote_iframe)
        self.scroll_page(direction='down')
        self.wait_element_to_be_visible(*self.locator.elms_skus_comments_input_box)
        self.wait_element_to_be_clickable(*self.locator.elms_skus_submit_button)

    @_step
    @allure.step('Wait for request form to be visible on page')
    def wait_request_form_to_be_visible(self, locator):
        self.wait_element_to_be_visible(*locator)
