import allure
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.locators import HomePageLocators


@pytest.mark.usefixtures('setup', 'website_setup')
class TestSitePages:
    reruns = 2
    reruns_delay = 2

    @pytest.mark.dependency(name="login", scope="session")
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

    @pytest.mark.dependency(depends=["login"], scope="session")
    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Open consumable state table')
    @allure.description('This is test of open consumable state table')
    def test_open_consumable_state_table(self, config):
        home_page = HomePage(self.driver, config)
        home_page.open_page(wait_element=HomePageLocators.logo_img)
        home_page.search_org('YMTC')
        home_page.open_org_dashboard()
        home_page.open_instrument_group_dashboard()
        assert 'Aperture Strip' in home_page.find_element(*HomePageLocators.aperture_strip_cell).text
