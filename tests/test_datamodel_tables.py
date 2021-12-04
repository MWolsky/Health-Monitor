import datetime
import pandas as pd
from config.constants import default_strava_cardio_training_types
from core.transformers.datamodel_tables import CardioTable, WeightsTable, LapsTable, DateTable
from tests.conftest import *
from core.transformers.strava_models import DetailedActivity, SummaryActivity, Lap
from core.transformers.filters import StravaFilter, StravaCardioTrainingFilter, StravaWeightTrainingFilter


class TestDataModelTables:
    def test_cardio_table(self, strava_models_detailed_activity_list):
        strava_filter = StravaFilter()
        cardio_filter = StravaCardioTrainingFilter()
        filtered_activities = [strava_filter.filter_detailed_activity(i) for i in strava_models_detailed_activity_list]
        activities = [DetailedActivity(**act) for act in filtered_activities]
        cardio_activities = cardio_filter.filter(activities)
        table_obj = CardioTable(cardio_activities)
        table = table_obj.cardio_table()

        assert isinstance(table_obj, CardioTable)
        assert len(table_obj.cardio_detailed_activities) == 18
        assert isinstance(table, pd.DataFrame)
        assert len(table) == 18
        assert len(table) == table['activity_id'].nunique()
        assert not table['activity_id'].isnull().values.any()
        assert all(isinstance(x, int) for x in table.activity_id)
        assert all(x for x in table.type if x in default_strava_cardio_training_types)
        assert len(table['activity_start_time'][0]) == 8
        assert len(table['date'][0]) == 10

    def test_laps_table(self, strava_models_lap_list):
        strava_filter = StravaFilter()
        filtered_activities = [strava_filter.filter_lap(i) for i in strava_models_lap_list]
        laps = [Lap(**act) for act in filtered_activities]
        table_obj = LapsTable(laps)
        table = table_obj.laps_table()

        assert isinstance(table_obj, LapsTable)
        assert len(table_obj.laps) == 11
        assert isinstance(table, pd.DataFrame)
        assert len(table) == 11
        assert len(table) == table['lap_id'].nunique()
        assert not table['lap_id'].isnull().values.any()
        assert all(isinstance(x, int) for x in table.lap_id)

    def test_weights_table(self, strava_models_summary_activity_list):
        strava_filter = StravaFilter()
        cardio_filter = StravaWeightTrainingFilter()
        filtered_activities = [strava_filter.filter_summary_activity(i) for i in strava_models_summary_activity_list]
        activities = [SummaryActivity(**act) for act in filtered_activities]
        cardio_activities = cardio_filter.filter(activities)
        table_obj = WeightsTable(cardio_activities)
        table = table_obj.weights_table()

        assert isinstance(table_obj, WeightsTable)
        assert len(table_obj.weights_activities) == 16
        assert isinstance(table, pd.DataFrame)
        assert len(table) == 16
        assert len(table) == table['activity_id'].nunique()
        assert not table['activity_id'].isnull().values.any()
        assert all(isinstance(x, int) for x in table.activity_id)
        assert all(x for x in table.type if x == 'WeightTraining')
        assert len(table['activity_start_time'][0]) == 8
        assert len(table['date'][0]) == 10

    def test_date_table(self):
        start_date = '2000-01-01'
        end_date = '2010-01-01'
        date_table_obj = DateTable(start_date, end_date)
        date_table = date_table_obj.date_table()

        assert isinstance(date_table, pd.DataFrame)
        assert len(date_table) == 3654
        assert all(isinstance(x, str) for x in date_table.date)
