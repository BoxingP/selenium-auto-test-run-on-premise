import allure
import pytest
from decouple import config as decouple_config

from apis.tf_api import TfAPI
from databases.e1_database import E1Database
from pages.home_page import HomePage
from pages.locators import HomePageLocators, RequestQuotePageLocators
from pages.login_page import LoginPage
from pages.request_quote_page import RequestQuotePage


@pytest.mark.usefixtures('setup')
class TestLoginPage:
    reruns = decouple_config('RERUNS', cast=int)
    reruns_delay = decouple_config('RERUNS_DELAY', cast=int)

    @pytest.mark.usefixtures('screenshot_on_failure')
    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Login test')
    @allure.description('This is test of login')
    def test_login(self):
        home_page = HomePage(self.driver)
        home_page.open_page(url=f"cn/zh/home.html?cid={decouple_config('CID')}", wait_element=HomePageLocators.logo_img)
        if not home_page.is_user_logged_in():
            home_page.go_to_login_page()
            login_page = LoginPage(self.driver)
            login_page.login('general', is_valid=True)
            login_page.redirect_to_home()
        profile_msg = '账户'
        assert profile_msg in home_page.find_element(*HomePageLocators.logged_in_menu).text
        home_page.logout()


class TestOrder:
    reruns = decouple_config('RERUNS', cast=int)
    reruns_delay = decouple_config('RERUNS_DELAY', cast=int)

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


@pytest.mark.usefixtures('setup')
class TestRequestQuotePage:
    reruns = decouple_config('RERUNS', cast=int)
    reruns_delay = decouple_config('RERUNS_DELAY', cast=int)

    @pytest.mark.parametrize('sku_value', decouple_config('ELMS_SKUS', cast=lambda v: v.split(',')))
    @pytest.mark.usefixtures('screenshot_on_failure')
    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Check elms skus request quote page opens normally test')
    @allure.description('This is test to check elms skus request quote page opens normally')
    def test_request_quote_page_for_elms_skus(self, sku_value):
        request_quote_page = RequestQuotePage(self.driver)
        request_quote_page.open_page(
            url=decouple_config('ELMS_URL').format(sku_value=sku_value, cid_value=decouple_config('CID')),
            wait_element=RequestQuotePageLocators.elms_skus_inquiry_title
        )
        request_quote_page.wait_elms_skus_request_form_visible()
        informed_msg = '我希望收到'
        assert informed_msg in request_quote_page.find_element(*RequestQuotePageLocators.elms_skus_informed_msg).text

    @pytest.mark.parametrize('sku_value', decouple_config('CATALOG_SKUS', cast=lambda v: v.split(',')))
    @pytest.mark.usefixtures('screenshot_on_failure')
    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Check catalog skus request quote page opens normally test')
    @allure.description('This is test to check catalog skus request quote page opens normally')
    def test_request_quote_page_for_catalog_skus(self, sku_value):
        request_quote_page = RequestQuotePage(self.driver)
        request_quote_page.open_page(
            url=decouple_config('CATALOG_URL').format(sku_value=sku_value, cid_value=decouple_config('CID')),
            wait_element=RequestQuotePageLocators.catalog_skus_inquiry_title
        )
        request_quote_page.wait_request_form_to_be_visible(RequestQuotePageLocators.catalog_skus_request_quote_form)
        title_msg = '名'
        assert title_msg in request_quote_page.find_element(
            *RequestQuotePageLocators.catalog_skus_first_name_title).text

    @pytest.mark.usefixtures('screenshot_on_failure')
    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Check bulk and custom product request quote page opens normally test')
    @allure.description('This is test to check bulk and custom product request quote page opens normally')
    def test_request_quote_page_for_bulk(self):
        request_quote_page = RequestQuotePage(self.driver)
        request_quote_page.open_page(
            url=decouple_config('BULK_URL').format(cid_value=decouple_config('CID')),
            wait_element=RequestQuotePageLocators.bulk_inquiry_title
        )
        request_quote_page.wait_request_form_to_be_visible(RequestQuotePageLocators.bulk_request_quote_form)
        title_msg = 'First Name'
        assert title_msg in request_quote_page.find_element(*RequestQuotePageLocators.bulk_first_name_title).text

    @pytest.mark.usefixtures('screenshot_on_failure')
    @pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
    @allure.title('Check analysis request quote page opens normally test')
    @allure.description('This is test to check analysis request quote page opens normally')
    def test_request_quote_page_for_analysis(self):
        request_quote_page = RequestQuotePage(self.driver)
        request_quote_page.open_page(
            url=decouple_config('ANALYSIS_URL').format(cid_value=decouple_config('CID')),
            wait_element=RequestQuotePageLocators.analysis_inquiry_title
        )
        request_quote_page.wait_request_form_to_be_visible(RequestQuotePageLocators.analysis_request_quote_form)
        title_msg = '姓名'
        assert title_msg in request_quote_page.find_element(*RequestQuotePageLocators.analysis_name_title).text
