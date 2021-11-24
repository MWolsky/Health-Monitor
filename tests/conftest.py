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
    resource = load_test_resource('strava_detailed_activity_list.json')
    return resource
