import datetime
from config.constants import project_start, project_end
from core.transformers.filters import StravaFilter, StravaCardioTrainingFilter, StravaWeightTrainingFilter
from core.transformers.datamodel_tables import CardioTable, LapsTable, WeightsTable, DateTable, CaloriesTable,\
    MealsDailyTable
from core.transformers.myfitnesspal_models import MyDay
from core.transformers.strava_models import Lap
from core.extractors.strava import StravaExtractor
from core.extractors.my_fitness_pal import MfpExtractor


def strava_tables(after: str = None, before: str = None):
    """Extract all summary activities in given period on the account and retrieves activity ids to request
    detailed activities. Filters response to cardio and weights trainings. Create dataframes for
    Cardio table, Weight table and Laps table.
    If params omitted, whole history of activities is extracted and tables created.
    :param after: date in YYYY-MM-DD
    :param before: date in YYYY-MM-DD """
    strava = StravaExtractor()
    strava_response_filter = StravaFilter()
    summary_activities = strava.all_summary_activities(after, before)
    activity_ids = [strava.get_activity_id_from_summary_activity(i) for i in summary_activities]
    detailed_activities = [strava.detailed_activity(i) for i in activity_ids]
    cardio_filter = StravaCardioTrainingFilter()
    weights_filter = StravaWeightTrainingFilter()
    cardio_activities = cardio_filter.filter(detailed_activities)
    cardio_laps = [i.laps for i in cardio_activities]
    cardio_laps_flatten = [strava_response_filter.filter_lap(lap) for act in cardio_laps for lap in act]
    cardio_laps_obj = [Lap(**i) for i in cardio_laps_flatten]
    weights_activities = weights_filter.filter(detailed_activities)

    cardio_table = CardioTable(cardio_activities).cardio_table()
    laps_table = LapsTable(cardio_laps_obj).laps_table()
    weights_table = WeightsTable(weights_activities).weights_table()

    return {
        'cardio': cardio_table,
        'weights': weights_table,
        'laps': laps_table
    }


def my_fitness_pal_tables_history():
    start_date = datetime.datetime.strptime(project_start, '%Y-%m-%d')
    mfp = MfpExtractor()
    history = mfp.get_history_since(start_date)
    my_days = [MyDay(day) for day in history]
    meals = MealsDailyTable(my_days)
    calories = CaloriesTable(my_days)
    return {
        'meals': meals,
        'calories': calories
    }


def my_fitness_pal_tables_since(start_date: datetime.datetime):
    mfp = MfpExtractor()
    history = mfp.get_history_since(start_date)
    my_days = [MyDay(day) for day in history]
    meals = MealsDailyTable(my_days)
    calories = CaloriesTable(my_days)
    return {
        'meals': meals,
        'calories': calories
    }


def my_fitness_pal_tables_yesterday():
    mfp = MfpExtractor()
    history = mfp.get_yesterday()
    my_days = [MyDay(history)]
    meals = MealsDailyTable(my_days)
    calories = CaloriesTable(my_days)
    return {
        'meals': meals,
        'calories': calories
    }


def my_fitness_pal_tables_last_week():
    mfp = MfpExtractor()
    history = mfp.get_last_seven_days()
    my_days = [MyDay(day) for day in history]
    meals = MealsDailyTable(my_days)
    calories = CaloriesTable(my_days)
    return {
        'meals': meals,
        'calories': calories
    }


def date_table():
    return DateTable(project_start, project_end).date_table()

