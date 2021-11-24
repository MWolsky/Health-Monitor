import myfitnesspal
import datetime
from secret_manager import MyFitnessPalSecretManager


class MyFitnessPal:
    def __init__(self):
        self._secret_manager = MyFitnessPalSecretManager()
        self.client = myfitnesspal.Client(self._secret_manager.my_fitness_pal_username,
                                          self._secret_manager.my_fitness_pal_secret)

    def get_day(self, year: int, month: int, day: int):
        return self.client.get_date(year, month, day)

    def get_days_in_range(self, start_date: datetime.datetime, end_date: datetime.datetime):
        delta = end_date - start_date
        days = []
        for i in range(delta.days + 1):
            date = start_date + datetime.timedelta(days=i)
            day = self.get_day(date.year, date.month, date.day)
            days.append(day)
        return days
