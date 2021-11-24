import datetime
from config.tables import cardio_table_config, laps_table_config, weights_table_config
from typing import List
from core.transformers.strava_models import *
from core.transformers.myfitnesspal_models import MyDay
import pandas as pd


class CardioTable:
    def __init__(self,
                 cardio_detailed_activities: List[DetailedActivity]):
        self.cardio_detailed_activities = cardio_detailed_activities
        self.cardio_config = cardio_table_config

    def cardio_table(self):
        table_rows = []
        for act in self.cardio_detailed_activities:
            row = {
                f'{self.cardio_config.activity_id}': act.id,
                f'{self.cardio_config.date}': act.start_date,
                f'{self.cardio_config.type}': act.type,
                f'{self.cardio_config.distance}': act.distance,
                f'{self.cardio_config.name}': act.name,
                f'{self.cardio_config.average_cadence}': act.average_cadence,
                f'{self.cardio_config.average_heartrate}': act.average_heartrate,
                f'{self.cardio_config.average_speed}': act.average_speed,
                f'{self.cardio_config.elapsed_time}': act.elapsed_time,
                f'{self.cardio_config.max_speed}': act.max_speed,
                f'{self.cardio_config.max_heartrate}': act.max_heartrate,
                f'{self.cardio_config.moving_time}': act.moving_time,
                f'{self.cardio_config.total_elevation_gain}': act.total_elevation_gain
            }
            table_rows.append(row)
        return pd.DataFrame(table_rows)


class LapsTable:
    def __init__(self, laps: List[Lap]):
        self.laps = laps
        self.splits_config = laps_table_config

    def laps_table(self):
        table_rows = []
        for lap in self.laps:
            row = {
                f'{self.splits_config.lap_id}': lap.id,
                f'{self.splits_config.activity_id}': lap.activity.get('id'),
                f'{self.splits_config.name}': lap.name,
                f'{self.splits_config.average_cadence}': lap.average_cadence,
                f'{self.splits_config.average_heartrate}': lap.average_heartrate,
                f'{self.splits_config.average_speed}': lap.average_speed,
                f'{self.splits_config.distance}': lap.distance,
                f'{self.splits_config.elapsed_time}': lap.elapsed_time,
                f'{self.splits_config.lap_index}': lap.lap_index,
                f'{self.splits_config.max_speed}': lap.max_speed,
                f'{self.splits_config.max_heartrate}': lap.max_heartrate,
                f'{self.splits_config.moving_time}': lap.moving_time,
                f'{self.splits_config.split}': lap.split,
                f'{self.splits_config.total_elevation_gain}': lap.total_elevation_gain,
                f'{self.splits_config.pace}': lap.pace,
                f'{self.splits_config.difficulty_index}': lap.difficulty_index,
            }
            table_rows.append(row)
        return pd.DataFrame(table_rows)


class WeightsTable:
    def __init__(self, weights_activities: List[Union[SummaryActivity, DetailedActivity]]):
        self.weights_activities = weights_activities
        self.weights_config = weights_table_config

    def weights_table(self):
        table_rows = []
        for training in self.weights_activities:
            row = {
                f'{self.weights_config.activity_id}': training.id,
                f'{self.weights_config.date}': training.start_date,
                f'{self.weights_config.type}': training.type,
                f'{self.weights_config.name}': training.name,
                f'{self.weights_config.average_heartrate}': training.average_heartrate,
                f'{self.weights_config.distance}': training.distance,
                f'{self.weights_config.elapsed_time}': training.elapsed_time,
                f'{self.weights_config.max_heartrate}': training.max_heartrate,
                f'{self.weights_config.moving_time}': training.moving_time
            }
            table_rows.append(row)
        return pd.DataFrame(table_rows)


class CaloriesTable:
    def __init__(self, days: List[MyDay]):
        self.days = days

    def calories_table(self):
        pass


class DateTable:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

    def date_table(self):
        table = pd.DataFrame({'date': pd.date_range(self.start_date, self.end_date)})
        table['year'] = table.date.dt.year
        table['month'] = table.date.dt.month
        table['day'] = table.date.dt.day

        table['date'] = table['date'].dt.date
        return table
