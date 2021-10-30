import pytest
from core.transformers.strava_models import *
from core.transformers.filters import StravaFilter
from tests.conftest import *

class TestStravaModels:
    def test_summary_activity(self, strava_models_summary_activity_list):
        strava_filter = StravaFilter()
        data = [strava_filter.filter_summary_activity(i) for i in strava_models_summary_activity_list]
        object_list = [SummaryActivity(**activity) for activity in data]

        assert all(isinstance(obj, SummaryActivity) for obj in object_list)

    def test_detailed_activity(self, strava_models_detailed_activity):
        strava_filter = StravaFilter()
        data = strava_filter.filter_detailed_activity(strava_models_detailed_activity)
        obj = DetailedActivity(**data)

        assert isinstance(obj, DetailedActivity)

    def test_map(self, strava_models_map):
        strava_filter = StravaFilter()
        data = strava_filter.filter_map(strava_models_map)
        obj = Map(**data)

        assert isinstance(obj, Map)

    def test_segment_effort(self, strava_models_segment_effort_list):
        strava_filter = StravaFilter()
        data = [strava_filter.filter_segment_effort(i) for i in strava_models_segment_effort_list]
        object_list = [SegmentEffort(**activity) for activity in data]

        assert all(isinstance(obj, SegmentEffort) for obj in object_list)

    def test_split(self, strava_models_split_list):
        strava_filter = StravaFilter()
        data = [strava_filter.filter_split(i) for i in strava_models_split_list]
        object_list = [Split(**activity) for activity in data]

        assert all(isinstance(obj, Split) for obj in object_list)

    def test_lap(self, strava_models_lap_list):
        strava_filter = StravaFilter()
        data = [strava_filter.filter_lap(i) for i in strava_models_lap_list]
        object_list = [Lap(**activity) for activity in data]

        assert all(isinstance(obj, Lap) for obj in object_list)

    def test_best_effort(self, strava_models_best_efforts_list):
        strava_filter = StravaFilter()
        data = [strava_filter.filter_best_efforts(i) for i in strava_models_best_efforts_list]
        object_list = [BestEffort(**activity) for activity in data]

        assert all(isinstance(obj, BestEffort) for obj in object_list)

    def test_segment(self, strava_models_segment):
        strava_filter = StravaFilter()
        data = strava_filter.filter_segment(strava_models_segment)
        obj = Segment(**data)

        assert isinstance(obj, Segment)

    def test_totals(self, strava_models_totals_list):
        strava_filter = StravaFilter()
        data = [strava_filter.filter_totals(i) for i in strava_models_totals_list]
        object_list = [Totals(**activity) for activity in data]

        assert all(isinstance(obj, Totals) for obj in object_list)

