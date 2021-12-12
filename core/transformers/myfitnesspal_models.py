from myfitnesspal.day import Day, Meal, Entry, Exercise
from typing import List


class MyDay:
    def __init__(self, day: Day):
        self.day = day

    def flat_day(self):
        day = dict(
            date=self.day.date,
            goal_calories=self.day.goals.get('calories', 0),
            goal_carbohydrates=self.day.goals.get('carbohydrates', 0),
            goal_fat=self.day.goals.get('fat', 0),
            goal_protein=self.day.goals.get('protein', 0),
            goal_sodium=self.day.goals.get('sodium', 0),
            goal_sugar=self.day.goals.get('sugar', 0),
            total_calories=self.day.totals.get('calories', 0),
            exercise_adjustment=self.exercise_calories_sum(),
            total_carbohydrates=self.day.totals.get('carbohydrates', 0),
            total_fat=self.day.totals.get('fat', 0),
            total_protein=self.day.totals.get('protein', 0),
            total_sodium=self.day.totals.get('sodium', 0),
            total_sugar=self.day.totals.get('sugar', 0),
            calories_net=self.day.totals.get('calories', 0) - self.day.goals.get('calories', 0),
            carbohydrates_net=self.day.totals.get('carbohydrates', 0) - self.day.goals.get('carbohydrates', 0),
            fat_net=self.day.totals.get('fat', 0) - self.day.goals.get('fat', 0),
            protein_net=self.day.totals.get('protein', 0) - self.day.goals.get('protein', 0),
            sodium_net=self.day.totals.get('sodium', 0) - self.day.goals.get('sodium', 0),
            sugar_net=self.day.totals.get('sugar', 0) - self.day.goals.get('sugar', 0),
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
                    "total_calories":  totals.get('calories', 0),
                    "total_carbohydrates": totals.get('carbohydrates', 0),
                    "total_fat": totals.get('fat', 0),
                    "total_protein": totals.get('protein', 0),
                    "total_sodium": totals.get('sodium', 0),
                    "total_sugar": totals.get('sugar', 0),
                    "quantity": entry.quantity,
                    "unit": entry.unit
                }
                meals.append(entry_row)
        return meals

    def exercise_calories_sum(self):
        calories = 0
        exercises: List[Exercise] = self.day.exercises
        if exercises and not isinstance(exercises, str):
            for ex in exercises:
                if ex.entries:
                    for ent in ex.entries:
                        if ent.totals:
                            calories += ent.totals.get('calories burned', 0)
        return calories

