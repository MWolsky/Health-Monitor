import pandas as pd
import pytest
from core.utils.helpers import load_test_resource
from typing import List, Dict, Union


@pytest.fixture()
def strava_models_summary_activity_list():
    resource = load_test_resource('strava_summary_activity_list')
    return resource


@pytest.fixture()
def strava_models_detailed_activity():
    resource = load_test_resource('strava_detailed_activity')
    return resource


@pytest.fixture()
def strava_models_lap_list():
    resource = load_test_resource('strava_lap_list')
    return resource


@pytest.fixture()
def strava_models_map():
    resource = load_test_resource('strava_map')
    return resource


@pytest.fixture()
def strava_models_segment_effort_list():
    resource = load_test_resource('strava_segment_effort_list')
    return resource


@pytest.fixture()
def strava_models_split_list():
    resource = load_test_resource('strava_split_list')
    return resource


@pytest.fixture()
def strava_models_athlete_stats():
    resource = load_test_resource('strava_athlete_stats')
    return resource


@pytest.fixture()
def strava_models_best_efforts_list():
    resource = load_test_resource('strava_best_efforts_list')
    return resource


@pytest.fixture()
def strava_models_segment():
    resource = load_test_resource('strava_segment')
    return resource


@pytest.fixture()
def strava_models_totals_list():
    resource = load_test_resource('strava_totals_list')
    return resource


@pytest.fixture()
def strava_models_detailed_activity_list():
    resource = load_test_resource('strava_detailed_activity_list')
    return resource


@pytest.fixture()
def daily_timestamps():
    resource = load_test_resource('daily_timestamps')
    return resource


@pytest.fixture()
def quarter_hour_timestamps():
    resource = load_test_resource('quarter_hour_timestamps.json')
    return resource


@pytest.fixture()
def input_dataframe():
    rows = []
    for i in range(0, 10):
        data = {
            'column1': f'a_{i}',
            'column2': f'b_{i}',
            'column3': f'c_{i}',
        }
        rows.append(data)
    return pd.DataFrame(rows)


@pytest.fixture()
def target_dataframe():
    rows = []
    for i in range(8, 20):
        data = {
            'col1': f'a_{i}',
            'col2': f'b_{i}',
            'col3': f'c_{i}',
        }
        rows.append(data)
    return pd.DataFrame(rows)
