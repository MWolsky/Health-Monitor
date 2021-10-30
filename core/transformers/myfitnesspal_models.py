from myfitnesspal.day import Day


class MyDay:
    def __init__(self, day: Day):
        self.day = day

    def flat_day(self):
        day = dict(
            date=self.day.date,
            goal_calories=self.day.goals['calories'],
            goal_carbohydrates=self.day.goals['carbohydrates'],
            goal_fat=self.day.goals['fat'],
            goal_protein=self.day.goals['protein'],
            goal_sodium=self.day.goals['sodium'],
            goal_sugar=self.day.goals['sugar'],
            total_calories=self.day.totals['calories'],
            total_carbohydrates=self.day.totals['carbohydrates'],
            total_fat=self.day.totals['fat'],
            total_protein=self.day.totals['protein'],
            total_sodium=self.day.totals['sodium'],
            total_sugar=self.day.totals['sugar'],
            calories_net=self.day.totals['calories']-self.day.goals['calories'],
            carbohydrates_net=self.day.totals['carbohydrates']-self.day.goals['carbohydrates'],
            fat_net=self.day.totals['fat']-self.day.goals['fat'],
            protein_net=self.day.totals['protein']-self.day.goals['protein'],
            sodium_net=self.day.totals['sodium']-self.day.goals['sodium'],
            sugar_net=self.day.totals['sugar']-self.day.goals['sugar']
        )
        return day
