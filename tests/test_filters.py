from core.transformers.filters import *
from config.constants import strava
from tests.conftest import *


class TestStravaResponseFilter:
    strava_filter = StravaFilter()

    def test_filter_summary_activity(self, strava_models_summary_activity_list):
        response = strava_models_summary_activity_list[0]
        filtered_response = self.strava_filter.filter_summary_activity(response)
        assert isinstance(filtered_response, dict)
        assert all(k in filtered_response.keys() for k in strava.summary_activity_keys)

    def test_filter_detailed_activity(self, strava_models_detailed_activity):
        filtered_response = self.strava_filter.filter_detailed_activity(strava_models_detailed_activity)
        assert isinstance(filtered_response, dict)
        assert all(k in filtered_response.keys() for k in strava.detailed_activity_keys)

    def test_filter_map(self, strava_models_map):
        filtered_response = self.strava_filter.filter_map(strava_models_map)
        assert isinstance(filtered_response, dict)
        assert all(k in filtered_response.keys() for k in strava.map_keys)

    def test_filter_segment_effort(self, strava_models_segment_effort_list):
        response = strava_models_segment_effort_list[0]
        filtered_response = self.strava_filter.filter_segment_effort(response)
        assert isinstance(filtered_response, dict)
        assert all(k in filtered_response.keys() for k in strava.segment_effort_keys)

    def test_filter_split(self, strava_models_split_list):
        response = strava_models_split_list[0]
        filtered_response = self.strava_filter.filter_split(response)
        assert isinstance(filtered_response, dict)
        assert all(k in filtered_response.keys() for k in strava.split_keys)

    def test_filter_lap(self, strava_models_lap_list):
        response = strava_models_lap_list[0]
        filtered_response = self.strava_filter.filter_lap(response)
        assert isinstance(filtered_response, dict)
        assert all(k in filtered_response.keys() for k in strava.lap_keys)

    def test_filter_best_efforts(self, strava_models_best_efforts_list):
        response = strava_models_best_efforts_list[0]
        filtered_response = self.strava_filter.filter_best_efforts(response)
        assert isinstance(filtered_response, dict)
        assert all(k in filtered_response.keys() for k in strava.best_efforts_keys)

    def test_filter_segment(self, strava_models_segment_effort_list):
        response = strava_models_segment_effort_list[0]
        filtered_response = self.strava_filter.filter_segment_effort(response)
        assert isinstance(filtered_response, dict)
        assert all(k in filtered_response.keys() for k in strava.segment_effort_keys)

    def test_filter_athlete_stats(self, strava_models_athlete_stats):
        response = strava_models_athlete_stats
        filtered_response = self.strava_filter.filter_athlete_stats(response)
        assert isinstance(filtered_response, dict)
        assert all(k in filtered_response.keys() for k in strava.athlete_stats_keys)

    def test_filter_totals(self, strava_models_totals_list):
        response = strava_models_totals_list[0]
        filtered_response = self.strava_filter.filter_totals(response)
        assert isinstance(filtered_response, dict)
        assert all(k in filtered_response.keys() for k in strava.totals_keys)


class TestStravaTrainingTypesFilter:
    strava_response_filter = StravaFilter()

    def test_weight_training_filter(self, strava_models_summary_activity_list):
        filtered_response = [self.strava_response_filter.filter_summary_activity(i)
                             for i in strava_models_summary_activity_list]
        weight_trainings_filter = StravaWeightTrainingFilter()
        activity_objects = [SummaryActivity(**i) for i in filtered_response]
        weight_trainings = weight_trainings_filter.filter(activity_objects)
        assert len(weight_trainings) == 16
        assert all(True for i in weight_trainings if i.type == 'WeightTraining')

    def test_cardio_training_filter(self, strava_models_detailed_activity_list):
        filtered_response = [self.strava_response_filter.filter_detailed_activity(i)
                             for i in strava_models_detailed_activity_list]
        cardio_trainings_filter = StravaCardioTrainingFilter()
        activity_objects = [DetailedActivity(**i) for i in filtered_response]
        cardio_trainings = cardio_trainings_filter.filter(activity_objects)
        assert len(cardio_trainings) == 18
        assert sum([True for i in cardio_trainings if i.type == 'Swim']) == 3
        assert sum([True for i in cardio_trainings if i.type == 'Run']) == 14
        assert sum([True for i in cardio_trainings if i.type == 'Ride']) == 1
        assert sum([True for i in cardio_trainings if i.type == 'Hike']) == 0
