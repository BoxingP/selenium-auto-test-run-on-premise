import allure
import pytest
from decouple import config as decouple_config

from pages.home_page import HomePage
from pages.locators import HomePageLocators
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup')
class TestSitePages:
    reruns = decouple_config('RERUNS', cast=int)
    reruns_delay = decouple_config('RERUNS_DELAY', cast=int)

    @pytest.mark.usefixtures('screenshot_on_failure')
    @pytest.mark.dependency(name="login", scope="session")
    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Open customer portal home page')
    @allure.description('This is test of open customer portal home page')
    def test_open_home_page(self):
        home_page = HomePage(self.driver)
        home_page.open_page()
        if not home_page.is_user_logged_in():
            home_page.redirect_to_login()
            login_page = LoginPage(self.driver)
            login_page.login('admin', is_valid=True)
            login_page.redirect_to_home()
        assert home_page.is_element_exists(*HomePageLocators.loading_bar) or home_page.is_element_exists(
            *HomePageLocators.create_org_button)

    @pytest.mark.usefixtures('screenshot_on_failure')
    @pytest.mark.dependency(depends=["login"], scope="session")
    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Open consumable state table')
    @allure.description('This is test of open consumable state table')
    def test_open_consumable_state_table(self):
        home_page = HomePage(self.driver)
        home_page.open_page(wait_element=HomePageLocators.logo_img)
        home_page.search_org('YMTC')
        home_page.open_org_dashboard()
        home_page.open_instrument_group_dashboard()
        assert 'Aperture Strip' in home_page.find_element(*HomePageLocators.aperture_strip_cell).text
