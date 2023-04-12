import datetime

import allure
from sqlalchemy import select

from databases.database import Database
from databases.database_schema import E1OrderHeader
from utils.logger import _step
from utils.time_convert import datetime_to_jde_julian_date


class E1Database(Database):
    def __init__(self, name):
        super(E1Database, self).__init__(name)

    @_step
    @allure.step('Get latest order number from E1 report database')
    def get_latest_order_number(self) -> int:
        china_now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
        latest_order = select(E1OrderHeader.SHDOCO). \
            filter(E1OrderHeader.SHTRDJ >= datetime_to_jde_julian_date(china_now)). \
            filter_by(SHDCTO='SO', SHKCOO='00714', SHTKBY='GES       ', SHURCD='CC'). \
            order_by(E1OrderHeader.SHTRDJ.desc()).\
            order_by(E1OrderHeader.SHUPMJ.desc()).order_by(E1OrderHeader.SHTDAY.desc())
        result = self.session.execute(latest_order).first()
        if result is not None:
            return result.SHDOCO
        else:
            return 0
