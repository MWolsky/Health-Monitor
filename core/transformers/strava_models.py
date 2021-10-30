from dataclasses import dataclass
from typing import List, Dict, Union, Optional


@dataclass
class SummaryActivity:
    id: int
    name: str
    type: str
    external_id: str
    upload_id: int
    start_date: str
    start_date_local: str
    timezone: str
    distance: Union[int, float]
    moving_time: Union[int, float]
    elapsed_time: Union[int, float]
    total_elevation_gain: Union[int, float]
    map: 'Map'
    average_speed: Union[int, float]
    max_speed: Union[int, float]
    has_heartrate: bool
    average_heartrate: Optional[float] = None
    max_heartrate: Optional[float] = None
    average_cadence: Optional[float] = None
    achievement_count: Optional[int] = None
    start_latlng: Optional[list] = None
    end_latlng: Optional[list] = None
    elev_high: Optional[float] = None
    elev_low: Optional[float] = None
    workout_type: Optional[str] = None


@dataclass
class DetailedActivity:
    id: int
    name: str
    type: str
    external_id: str
    upload_id: int
    start_date: str
    start_date_local: str
    timezone: str
    distance: Union[int, float]
    moving_time: Union[int, float]
    elapsed_time: Union[int, float]
    total_elevation_gain: Union[int, float]
    map: 'Map'
    average_speed: Union[int, float]
    max_speed: Union[int, float]
    has_heartrate: bool
    description: str
    calories: float
    perceived_exertion: str
    prefer_perceived_exertion: str
    segment_efforts: List['SegmentEffort']
    splits_metric: List['Split']
    splits_standard: List['Split']
    laps: List['Lap']
    best_efforts: List['BestEffort']
    photos: dict
    stats_visibility: List[Dict]
    hide_from_home: bool
    similar_activities: dict
    available_zones: list
    device_name: Optional[str] = None
    average_heartrate: Optional[float] = None
    max_heartrate: Optional[float] = None
    average_cadence: Optional[float] = None
    achievement_count: Optional[int] = None
    start_latlng: Optional[list] = None
    end_latlng: Optional[list] = None
    elev_high: Optional[float] = None
    elev_low: Optional[float] = None
    workout_type: Optional[str] = None


@dataclass
class Map:
    id: str
    summary_polyline: str
    resource_state: int


class SegmentEffort:
    id: int
    resource_state: int
    name: str
    activity: dict
    athlete: dict
    elapsed_time: Union[int, float]
    moving_time: Union[int, float]
    start_date: str
    start_date_local: str
    distance: Union[int, float]
    start_index: int
    end_index: int
    average_cadence: float
    average_heartrate: float
    max_heartrate: float
    segment: 'Segment'
    pr_rank: Union[int, float, str]
    achievements: list
    hidden: bool


class Split:
    distance: Union[int, float]
    elapsed_time: Union[int, float]
    elevation_difference: Union[int, float]
    moving_time: Union[int, float]
    split: int
    average_speed: Union[int, float]
    average_grade_adjusted_speed: Union[int, float]
    average_heartrate: Union[int, float]
    pace_zone: int


class Lap:
    id: int
    resource_state: int
    name: str
    activity: dict
    athlete: dict
    elapsed_time: Union[int, float]
    moving_time: Union[int, float]
    start_date: str
    start_date_local: str
    distance: Union[int, float]
    start_index: Union[int, float]
    end_index: Union[int, float]
    total_elevation_gain: Union[int, float]
    average_speed: Union[int, float]
    max_speed: Union[int, float]
    average_cadence: Union[int, float]
    average_heartrate: Union[int, float]
    max_heartrate: Union[int, float]
    lap_index: int
    split: int
    pace_zone: int


class BestEffort:
    id: int
    resource_state: int
    name: str
    activity: dict
    athlete: dict
    elapsed_time: Union[int, float]
    moving_time: Union[int, float]
    start_date: str
    start_date_local: str
    distance: Union[int, float]
    start_index: Union[int, float]
    end_index: Union[int, float]
    pr_rank: Union[int, float, str]
    achievement: list


class Segment:
    id: int
    resource_state: int
    name: str
    activity_type: str
    distance: Union[int, float]
    average_grade: Union[int, float]
    maximum_grade: Union[int, float]
    elevation_high: Union[int, float]
    elevation_low: Union[int, float]
    start_latlng: list
    end_latlng: list
    elevation_profile: str
    start_latitude: float
    start_longitude: float
    end_latitude: float
    end_longitude: float
    climb_category: Union[int, float, str]
    city: str
    state: str
    country: str
    private: bool
    hazardous: bool
    starred: bool
