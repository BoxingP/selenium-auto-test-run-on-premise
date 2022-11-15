import allure
from selenium.webdriver.common.keys import Keys

from pages.page import Page
from utils.locators import HomePageLocators, SearchPageLocators
from utils.logger import _step


class HomePage(Page):
    def __init__(self, driver, config):
        super(HomePage, self).__init__(driver, config)
        self.locator = HomePageLocators

    @_step
    @allure.step('Search product {product}')
    def search_product(self, product):
        self.click(*self.locator.search_field)
        self.wait_url_changed_to('search')
        self.input_text(product, *SearchPageLocators.search_field)
        self.find_element(*SearchPageLocators.search_field).send_keys(Keys.ENTER)

    @_step
    @allure.step('Go to cart page')
    def go_to_cart_page(self):
        self.click(*self.locator.cart_link)
        self.wait_url_changed_to('my-cart')
