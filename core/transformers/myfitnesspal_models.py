from myfitnesspal.day import Day, Meal, Entry


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
            sugar_net=self.day.totals['sugar']-self.day.goals['sugar'],
            complete_day=1 if self.day.complete is True else 0
        )
        return day

    def flat_meals(self):
        meals = []
        for meal in self.day.meals:
            meal: Meal
            for entry in meal:
                entry: Entry
                totals: dict = entry.totals
                entry_row = {
                    "date": self.day.date,
                    "meal_type": meal.name,
                    "food_name": entry.name,
                    "total_calories":  totals['calories'],
                    "total_carbohydrates": totals['carbohydrates'],
                    "total_fat": totals['fat'],
                    "total_protein": totals['protein'],
                    "total_sodium": totals['sodium'],
                    "total_sugar": totals['sugar'],
                    "quantity": entry.quantity,
                    "unit": entry.unit
                }
                meals.append(entry_row)
        return meals



