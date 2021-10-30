import myfitnesspal


class MyFitnessPal:
    def __init__(self, username: str, password: str):
        self.client = myfitnesspal.Client(username, password)

    def get_day(self, year: int, month: int, day: int):
        return self.client.get_date(year, month, day)

