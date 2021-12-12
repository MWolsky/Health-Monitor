import myfitnesspal
import datetime
from secret_manager import MyFitnessPalSecretManager
from typing import List
from myfitnesspal.day import Day
from logging import getLogger
from core.utils.helpers import logging_config

logger = getLogger(__name__)
logging_config()


class MyFitnessPal:
    def __init__(self):
        self._secret_manager = MyFitnessPalSecretManager()
        self.client = myfitnesspal.Client(self._secret_manager.my_fitness_pal_username,
                                          self._secret_manager.my_fitness_pal_secret)

    def get_day(self, year: int, month: int, day: int) -> Day:
        """returns Day object for given day"""
        logger.info(f'Requesting: {datetime.datetime(year, month, day).strftime("%Y-%m-%d")}')
        return self.client.get_date(year, month, day)

    def get_days_in_range(self, start_date: datetime.datetime, end_date: datetime.datetime) -> List[Day]:
        """returns list of Days objects for given period"""
        delta = end_date - start_date
        days = []
        for i in range(delta.days + 1):
            date = start_date + datetime.timedelta(days=i)
            day = self.get_day(date.year, date.month, date.day)
            days.append(day)
            logger.info(f'Downloaded {i}/{delta.days + 1} days.')
        return days
