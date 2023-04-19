import allure
import pytest
from decouple import config

from apis.tf_api import TfAPI
from databases.e1_database import E1Database
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.locators import HomePageLocators


@pytest.mark.usefixtures('setup')
class TestSitePages:
    reruns = config('RERUNS', cast=int)
    reruns_delay = config('RERUNS_DELAY', cast=int)

    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Login test')
    @allure.description('This is test of login')
    def test_login(self):
        home_page = HomePage(self.driver)
        home_page.open_page(url=f"cn/zh/home.html?cid={config('CID')}", wait_element=HomePageLocators.logo_img)
        home_page.go_to_login_page()
        login_page = LoginPage(self.driver)
        login_page.login('general', is_valid=True)
        login_page.redirect_to_home()
        profile_msg = '账户'
        assert profile_msg in login_page.find_element(*HomePageLocators.logged_in_menu).text
        login_page.logout()

    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Check placed order appears in history test')
    @allure.description('This is test to check whether placed order will appear in order history')
    def test_placed_order_appears(self):
        e1_order = E1Database('E1_REPORT').get_latest_order_number()
        if e1_order == 0:
            assert True
        else:
            csr_order_details = TfAPI().get_order_details(str(e1_order))
            if csr_order_details is not None:
                assert e1_order == int(csr_order_details['salesOrderNumber'])
            else:
                assert False
