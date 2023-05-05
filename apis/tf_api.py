import json

import allure
from decouple import config as decouple_config

from apis.api import API
from utils.logger import _step


class TfAPI(API):
    def __init__(self):
        super(TfAPI, self).__init__()

    @_step
    @allure.step('Get order details from TF API')
    def get_order_details(self, order_number):
        return self.send_request(url=f"{decouple_config('ORDER_DETAILS_API')}{str(order_number)}",
                                 headers=decouple_config('ORDER_DETAILS_HEADERS', cast=lambda x: json.loads(x)))
