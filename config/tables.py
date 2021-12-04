from dataclasses import dataclass

_cardio_table_config_fields = {
    'activity_id': 'activity_id',
    'date': 'date',
    'activity_start_time': 'activity_start_time',
    'type': 'type',
    'distance': 'distance',
    'name': 'name',
    'average_cadence': 'average_cadence',
    'average_heartrate': 'average_heartrate',
    'average_speed': 'average_speed',
    'elapsed_time': 'elapsed_time',
    'max_speed': 'max_speed',
    'max_heartrate': 'max_heartrate',
    'moving_time': 'moving_time',
    'total_elevation_gain': 'total_elevation_gain'
}
_laps_table_config_fields = {
    'activity_id': 'activity_id',
    'lap_id': 'lap_id',
    'name': 'name',
    'average_cadence': 'average_cadence',
    'average_speed': 'average_speed',
    'average_heartrate': 'average_heartrate',
    'distance': 'distance',
    'elapsed_time': 'elapsed_time',
    'lap_index': 'lap_index',
    'max_speed': 'max_speed',
    'max_heartrate': 'max_heartrate',
    'moving_time': 'moving_time',
    'split': 'split',
    'total_elevation_gain': 'total_elevation_gain',
    'pace': 'pace',
    'difficulty_index': 'difficulty_index'
}
_weights_table_config_fields = {
    'activity_id': 'activity_id',
    'date': 'date',
    'activity_start_time': 'activity_start_time',
    'type': 'type',
    'name': 'name',
    'average_heartrate': 'average_heartrate',
    'distance': 'distance',
    'elapsed_time': 'elapsed_time',
    'max_heartrate': 'max_heartrate',
    'moving_time': 'moving_time'
}


@dataclass
class WeightsConfig:
    activity_id: str
    date: str
    activity_start_time: str
    type: str
    name: str
    average_heartrate: str
    distance: str
    elapsed_time: str
    max_heartrate: str
    moving_time: str


@dataclass
class CardioConfig:
    activity_id: str
    date: str
    activity_start_time: str
    type: str
    distance: str
    name: str
    average_cadence: str
    average_heartrate: str
    average_speed: str
    elapsed_time: str
    max_speed: str
    max_heartrate: str
    moving_time: str
    total_elevation_gain: str


@dataclass
class LapsConfig:
    activity_id: str
    lap_id: str
    name: str
    average_cadence: str
    average_speed: str
    average_heartrate: str
    distance: str
    elapsed_time: str
    lap_index: str
    max_speed: str
    max_heartrate: str
    moving_time: str
    split: str
    total_elevation_gain: str
    pace: float
    difficulty_index: str


cardio_table_config = CardioConfig(**_cardio_table_config_fields)
laps_table_config = LapsConfig(**_laps_table_config_fields)
weights_table_config = WeightsConfig(**_weights_table_config_fields)
