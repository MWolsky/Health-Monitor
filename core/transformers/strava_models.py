from dataclasses import dataclass, field
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

    @property
    def activity_date(self):
        return self.start_date_local[:10]

    @property
    def activity_time(self):
        return self.start_date_local[11:-1]


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
    photos: dict
    stats_visibility: List[Dict]
    hide_from_home: bool
    available_zones: list
    laps: List['Lap'] = None
    similar_activities: dict = None
    splits_metric: List['Split'] = None
    splits_standard: List['Split'] = None
    best_efforts: List['BestEffort'] = None
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

    @property
    def activity_date(self):
        return self.start_date_local[:10]

    @property
    def activity_time(self):
        return self.start_date_local[11:-1]

@dataclass
class Map:
    id: str
    summary_polyline: str
    resource_state: int


@dataclass
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


@dataclass
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


@dataclass
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
    lap_index: int
    split: int
    average_heartrate: Union[int, float] = None
    max_heartrate: Union[int, float] = None
    pace_zone: int = None
    average_cadence: Union[int, float] = None

    @property
    def pace(self):
        """returns pace in mins / km"""
        return 1000 / self.average_speed / 60

    @property
    def difficulty_index(self):
        lap_distance_weight = 0.001
        pace_weight = 0.5
        elevation_gain_weight = 0.25
        lap_index_weight = 0.249
        pace_points = self.pace_points(self.pace)

        difficulty_index = self.distance * lap_distance_weight + \
            pace_points * pace_weight + self.total_elevation_gain * elevation_gain_weight + \
            self.lap_index * lap_index_weight
        return difficulty_index

    @staticmethod
    def pace_points(pace: float):
        if pace >= 6.5:
            return 0.1
        elif 6 <= pace < 6.5:
            return 0.5
        elif 5.5 <= pace < 6:
            return 1
        elif 5 <= pace < 5.5:
            return 3
        elif 4.5 <= pace < 5:
            return 6
        elif 4.0 <= pace < 4.5:
            return 9
        else:
            return 10

@dataclass
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
    achievements: list


@dataclass
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


@dataclass
class AthleteStats:
    biggest_ride_distance: Union[int, float]
    biggest_climb_elevation_gain: Union[int, float]
    recent_ride_totals: 'Totals'
    all_ride_totals: 'Totals'
    recent_run_totals: 'Totals'
    all_run_totals: 'Totals'
    recent_swim_totals: 'Totals'
    all_swim_totals: 'Totals'
    ytd_ride_totals: 'Totals'
    ytd_run_totals: 'Totals'
    ytd_swim_totals: 'Totals'


@dataclass
class Totals:
    count: int
    distance: Union[int, float]
    moving_time: Union[int, float]
    elapsed_time: Union[int, float]
    elevation_gain: Union[int, float]
    achievement_count: int = None

