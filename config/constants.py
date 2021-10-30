from dataclasses import dataclass
from typing import List


@dataclass
class StravaResponseConfig:
    profile_id: int
    summary_activity_keys: List[str]
    detailed_activity_keys: List[str]
    map_keys: List[str]
    segment_effort_keys: List[str]
    split_keys: List[str]
    lap_keys: List[str]
    best_efforts_keys: List[str]
    segment_keys: List[str]
    athlete_stats_keys: List[str]
    totals_keys: List[str]


strava_config = {
    'profile_id': 77615538,
    'summary_activity_keys': [
        'id',
        'name',
        'type',
        'external_id',
        'upload_id',
        'start_date',
        'start_date_local',
        'timezone',
        'distance',
        'moving_time',
        'elapsed_time',
        'total_elevation_gain',
        'map',
        'average_speed',
        'max_speed',
        'has_heartrate',
        'average_heartrate',
        'max_heartrate',
        'average_cadence',
        'achievement_count',
        'start_latlng',
        'end_latlng',
        'elev_high',
        'elev_low',
        'workout_type'
    ],
    'detailed_activity_keys': [
        'id',
        'name',
        'type',
        'external_id',
        'upload_id',
        'start_date',
        'start_date_local',
        'timezone',
        'distance',
        'moving_time',
        'elapsed_time',
        'total_elevation_gain',
        'map',
        'average_speed',
        'max_speed',
        'has_heartrate',
        'average_heartrate',
        'max_heartrate',
        'average_cadence',
        'achievement_count',
        'start_latlng',
        'end_latlng',
        'elev_high',
        'elev_low',
        'workout_type',
        'description',
        'calories',
        'perceived_exertion',
        'prefer_perceived_exertion',
        'segment_efforts',
        'splits_metric',
        'splits_standard',
        'laps',
        'best_efforts',
        'photos',
        'stats_visibility',
        'hide_from_home',
        'similar_activities',
        'available_zones',
        'device_name'
    ],
    'map_keys': [
        'id',
        'summary_polyline',
        'resource_state'
    ],
    'segment_effort_keys': [
        'id',
        'resource_state',
        'name',
        'activity',
        'athlete',
        'elapsed_time',
        'moving_time',
        'start_date',
        'start_date_local',
        'distance',
        'start_index',
        'end_index',
        'average_cadence',
        'average_heartrate',
        'max_heartrate',
        'segment',
        'pr_rank',
        'achievements',
        'hidden'
    ],
    'split_keys': [
        'distance',
        'elapsed_time',
        'elevation_difference',
        'moving_time',
        'split',
        'average_speed',
        'average_grade_adjusted_speed',
        'average_heartrate',
        'pace_zone'
    ],
    'lap_keys': [
        'id',
        'resource_state',
        'name',
        'activity',
        'athlete',
        'elapsed_time',
        'moving_time',
        'start_date',
        'start_date_local',
        'distance',
        'start_index',
        'end_index',
        'total_elevation_gain',
        'average_speed',
        'max_speed',
        'average_cadence',
        'average_heartrate',
        'max_heartrate',
        'lap_index',
        'split',
        'pace_zone'
    ],
    'best_efforts_keys': [
        'id',
        'resource_state',
        'name',
        'activity',
        'athlete',
        'elapsed_time',
        'moving_time',
        'start_date',
        'start_date_local',
        'distance',
        'start_index',
        'end_index',
        'pr_rank',
        'achievements'
    ],
    'athlete_stats_keys': [
        'biggest_ride_distance',
        'biggest_climb_elevation_gain',
        'recent_ride_totals',
        'all_ride_totals',
        'recent_run_totals',
        'all_run_totals',
        'recent_swim_totals',
        'all_swim_totals',
        'ytd_ride_totals',
        'ytd_run_totals',
        'ytd_swim_totals'
    ],
    'totals_keys': [
        'count',
        'distance',
        'moving_time',
        'elapsed_time',
        'elevation_gain',
        'achievement_count'
    ],
    'segment_keys': [
        'id',
        'resource_state',
        'name',
        'activity_type',
        'distance',
        'average_grade',
        'maximum_grade',
        'elevation_high',
        'elevation_low',
        'start_latlng',
        'end_latlng',
        'elevation_profile',
        'start_latitude',
        'start_longitude',
        'end_latitude',
        'end_longitude',
        'climb_category',
        'city',
        'state',
        'country',
        'private',
        'hazardous',
        'starred',
    ]
}

strava = StravaResponseConfig(**strava_config)
