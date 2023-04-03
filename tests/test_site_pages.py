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
    @allure.title('Login test')
    @allure.description('This is test of login')
    def test_login(self, config):
        home_page = HomePage(self.driver, config)
        home_page.open_page(url=f"cn/zh/home.html?cid={config['cid']}", wait_element=HomePageLocators.logo_img)
        home_page.go_to_login_page()
        login_page = LoginPage(self.driver, config)
        login_page.login('general', is_valid=True)
        login_page.redirect_to_home()
        profile_msg = '账户'
        assert profile_msg in login_page.find_element(*HomePageLocators.logged_in_menu).text
        login_page.logout()
