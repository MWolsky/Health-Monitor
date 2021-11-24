from core.connectors.strava import Strava
from core.connectors.myfitnesspal import MyFitnessPal
from core.transformers.filters import StravaFilter, StravaCardioTrainingFilter, StravaWeightTrainingFilter
from core.transformers.datamodel_tables import CardioTable, LapsTable, WeightsTable, DateTable
from core.transformers.strava_models import Lap
from core.extractors.strava import StravaExtractor


def strava_tables(after: str = None, before: str = None):
    """Extract all summary activities on the account and retrieves activity ids to request
    detailed activities. Filters response to cardio and weights trainings. Create dataframes for
    Cardio table, Weight table and Laps table"""
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

    return {'cardio': cardio_table,
            'weights': weights_table,
            'laps': laps_table}


def calories_table():
    mfp = MyFitnessPal()
    day = mfp.get_day(2021, 11, 1)
    return day

if __name__ == "__main__":
    t = calories_table()