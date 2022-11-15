import time

import allure
import pytest

from pages.home_page import HomePage
from utils.locators import SearchPageLocators, ProductPageLocators, CartPageLocators, OrderPageLocators
from utils.logger import _step


@pytest.mark.usefixtures('setup', 'website_setup')
class TestCartPage:
    reruns = 2
    reruns_delay = 2

    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @_step
    @allure.title('Submit order test')
    @allure.description('This is test of submit order')
    def test_submit_order(self, config):
        cart_page = HomePage(self.driver, config)
        cart_page.open_page('')
        cart_page.wait_url_changed_to('home')
        cart_page.search_product('K1622')
        cart_page.wait_element_to_be_visible(*SearchPageLocators.result)
        cart_page.click(*SearchPageLocators.first_result)
        cart_page.wait_url_changed_to('product-details')
        cart_page.click(*ProductPageLocators.add_to_cart_button)
        cart_page.wait_element_to_be_visible(*ProductPageLocators.added_to_cart_msg)
        cart_page.click(*ProductPageLocators.cart_link)
        cart_page.wait_url_changed_to('my-cart')
        time.sleep(3)
        cart_page.click(*CartPageLocators.edit_ship_to)
        cart_page.wait_url_changed_to('DeliveryAddress')
        cart_page.click(*CartPageLocators.ship_to_field)
        time.sleep(3)
        time.sleep(3)
        cart_page.click(*CartPageLocators.settle_order_button)
        cart_page.wait_url_changed_to('submit-order')
        cart_page.input_text('15800000000', *CartPageLocators.ship_to_phone_field)
        cart_page.input_text('15800000000', *CartPageLocators.bill_to_phone_field)
        cart_page.scroll_page('down')
        time.sleep(3)
        cart_page.click(*CartPageLocators.disclaimer)
        cart_page.click(*CartPageLocators.submit_order_button)
        cart_page.wait_url_changed_to('success')
        order_number = cart_page.find_element(*CartPageLocators.order_number).text
        cart_page.click(*CartPageLocators.my_order)
        cart_page.wait_url_changed_to('my-orders')
        cart_page.wait_element_to_be_visible(*OrderPageLocators.my_order)
        assert order_number in cart_page.find_element(*OrderPageLocators.order_number).text
