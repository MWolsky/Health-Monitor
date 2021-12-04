from core.connectors.myfitnesspal import MyFitnessPal
from myfitnesspal.day import Day
import datetime
from typing import List


class MfpExtractor:
    def __init__(self):
        self.con = MyFitnessPal()

    @staticmethod
    def __yesterday() -> datetime.datetime:
        """returns datetime object of yesterday"""
        return datetime.datetime.now() - datetime.timedelta(days=1)

    def get_yesterday(self) -> Day:
        """returns Day object from MyFitnessPal of yesterday"""
        date = self.__yesterday()
        return self.con.get_day(date.year, date.month, date.day)

    def get_last_seven_days(self) -> List[Day]:
        """returns list of Days objects for last 7 days ending yesterday"""
        start_day = datetime.datetime.now() - datetime.timedelta(days=7)
        yesterday = self.__yesterday()
        return self.con.get_days_in_range(start_day, yesterday)

    def get_history_since(self, start_day: datetime.datetime) -> List[Day]:
        """returns list of Days objects created since start_day"""
        return self.con.get_days_in_range(start_day, datetime.datetime.now())

