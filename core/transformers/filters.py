from config.constants import strava, default_strava_cardio_training_types
from typing import Dict, List, Union
from core.transformers.strava_models import DetailedActivity, SummaryActivity


class StravaFilter:
    @staticmethod
    def filter_summary_activity(response: Dict):
        keys = strava.summary_activity_keys
        filtered_response = {k: v for k, v in response.items() if k in keys}
        return filtered_response

    @staticmethod
    def filter_detailed_activity(response: Dict):
        keys = strava.detailed_activity_keys
        filtered_response = {k: v for k, v in response.items() if k in keys}
        return filtered_response

    @staticmethod
    def filter_map(response: Dict):
        keys = strava.map_keys
        filtered_response = {k: v for k, v in response.items() if k in keys}
        return filtered_response

    @staticmethod
    def filter_segment_effort(response: Dict):
        keys = strava.segment_effort_keys
        filtered_response = {k: v for k, v in response.items() if k in keys}
        return filtered_response

    @staticmethod
    def filter_split(response: Dict):
        keys = strava.split_keys
        filtered_response = {k: v for k, v in response.items() if k in keys}
        return filtered_response

    @staticmethod
    def filter_lap(response: Dict):
        keys = strava.lap_keys
        filtered_response = {k: v for k, v in response.items() if k in keys}
        return filtered_response

    @staticmethod
    def filter_best_efforts(response: Dict):
        keys = strava.best_efforts_keys
        filtered_response = {k: v for k, v in response.items() if k in keys}
        return filtered_response

    @staticmethod
    def filter_segment(response: Dict):
        keys = strava.segment_keys
        filtered_response = {k: v for k, v in response.items() if k in keys}
        return filtered_response

    @staticmethod
    def filter_athlete_stats(response: Dict):
        keys = strava.athlete_stats_keys
        filtered_response = {k: v for k, v in response.items() if k in keys}
        return filtered_response

    @staticmethod
    def filter_totals(response: Dict):
        keys = strava.totals_keys
        filtered_response = {k: v for k, v in response.items() if k in keys}
        return filtered_response


class StravaTrainingTypeFilter:
    def apply_filter(self, activity: [Union[DetailedActivity, SummaryActivity]]):
        raise NotImplementedError

    def filter(self, activities: List[Union[DetailedActivity, SummaryActivity]]):
        return list(filter(self.apply_filter, activities))


class StravaWeightTrainingFilter(StravaTrainingTypeFilter):
    def apply_filter(self, activity: [Union[DetailedActivity, SummaryActivity]]):
        activity_type_filter = activity.type == 'WeightTraining'
        filters = [activity_type_filter]
        return all(filters)


class StravaCardioTrainingFilter(StravaTrainingTypeFilter):
    def apply_filter(self, activity: [Union[DetailedActivity, SummaryActivity]]):
        activity_type_filter = activity.type in default_strava_cardio_training_types
        filters = [activity_type_filter]
        return all(filters)
