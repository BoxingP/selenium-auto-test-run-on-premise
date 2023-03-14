import allure
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.locators import HomePageLocators


@pytest.mark.usefixtures('setup', 'website_setup')
class TestSitePages:
    reruns = 2
    reruns_delay = 2

    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Open customer portal home page')
    @allure.description('This is test of open customer portal home page')
    def test_open_home_page(self, config):
        home_page = HomePage(self.driver, config)
        home_page.open_page()
        home_page.redirect_to_login()
        login_page = LoginPage(self.driver, config)
        login_page.login('admin', is_valid=True)
        login_page.redirect_to_home()
        assert home_page.is_element_exists(*HomePageLocators.loading_bar) or home_page.is_element_exists(
            *HomePageLocators.create_org_button)
