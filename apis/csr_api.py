import allure

from apis.api import API
from utils.logger import _step


class CsrAPI(API):
    def __init__(self, name):
        super(CsrAPI, self).__init__(name)

    @_step
    @allure.step('Get order details from CSR API')
    def get_order_details(self, order_number):
        api = [api for api in self.config['api'] if api['name'] == 'get order details'][0]
        return self.send_request(url=f"{api['url']}{str(order_number)}", headers=api['headers'])
