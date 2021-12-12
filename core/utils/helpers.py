import time
import core.utils.directories as hlp
import json
import datetime
import math
import pytz
from logging import getLogger
from logging.config import dictConfig
import toml
from typing import List


def load_pyproject_toml():
    file_dir = hlp.pyproject_toml_dir()
    if file_dir.exists():
        toml_dict = toml.load(file_dir)
    else:
        raise NotADirectoryError('No such directory of pyproject toml.')
    return toml_dict


def logging_config():
    logging_dict = load_pyproject_toml()['tool']['logging']
    dictConfig(logging_dict)


logging_config()
logger = getLogger(__name__)


def open_sql_file(filename: str) -> str:
    fullname = filename + '.sql'
    with open (hlp.sqlcommands_dir().joinpath(fullname)) as file:
        f = file.read()
        return f


def date_to_unix_timestamp(date: str, utc: bool = False) -> int:
    """converts date in yyyy-mm-dd format to unix timestmap"""
    if utc is False:
        timestamp = datetime.datetime.strptime(date, "%Y-%m-%d").timestamp()
    else:
        timestamp = datetime.datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc).timestamp()
    return round(timestamp)


def load_test_resource(resource_name: str):
    resource_path = hlp.resources_tests_dir().joinpath(resource_name).with_suffix('.json')
    with open(resource_path) as f:
        resource_file = json.load(f)
    return resource_file


def open_strava_logs():
    strava_logs_path = hlp.strava_api_logs_dir()
    with open(strava_logs_path) as f:
        file = json.load(f)
    return file


def save_strava_logs(logs_list: list):
    strava_logs_path = hlp.strava_api_logs_dir()
    with open(strava_logs_path, 'w') as f:
        json.dump(logs_list, f, indent=4, sort_keys=True, default=str)
    return True


def daily_timestamp_counter(timestamp_list: List[datetime.datetime], limit: int):
    """
    :param timestamp_list: list of datetime.datetime objects (utc) formated as strings
    :param limit: daily limit of timestamps
    :return: True if limit not reached, False if reached
    """
    today = datetime.datetime.now(tz=pytz.utc).day
    days = [x.date() for x in timestamp_list if x.day == today]
    if len(days) < limit:
        return True, len(days)
    else:
        return False, len(days)


def quarter_an_hour_timestamp_counter(timestamp_list: List[datetime.datetime], limit: int):
    """
    :param timestamp_list: list of datetime.datetime objects (utc) formatted as strings
    :param limit: quarter of an hour limit of timestamps
    :return: True if limit not reached, False if reached
    """
    now = datetime.datetime.now(tz=pytz.utc).replace(tzinfo=None)
    if 0 <= now.minute < 15:
        quarter_before = 0
    elif 15 <= now.minute < 30:
        quarter_before = 15
    elif 30 <= now.minute < 45:
        quarter_before = 30
    else:
        quarter_before = 45

    if 0 <= now.minute < 15:
        quarter_next = 15
    elif 15 <= now.minute < 30:
        quarter_next = 30
    elif 30 <= now.minute < 45:
        quarter_next = 45
    else:
        quarter_next = 60

    relevant = [x for x in timestamp_list if quarter_before <= x.minute < quarter_next and
                x.month == now.month and x.day == now.day and x.hour == now.hour]
    if len(relevant) < limit:
        return True, len(relevant)
    else:
        return False, len(relevant)


def next_quarter_of_hour():
    dt = datetime.datetime.now(pytz.utc)
    nsecs = dt.minute*60 + dt.second + dt.microsecond*1e-6

    delta = math.ceil(nsecs / 900) * 900 - nsecs

    return dt + datetime.timedelta(seconds=delta)


def sleep_till_next_quarter_of_hour():
    now = datetime.datetime.now(pytz.utc)
    next_quarter = next_quarter_of_hour()
    to_sleep = (next_quarter - now).seconds + 3
    logger.info(f'Now is {now}. \nNext quarter of an hour is {next_quarter}. \nSleeping: {to_sleep} seconds...')
    time.sleep(to_sleep)


def sleep_till_tomorrow():
    now = datetime.datetime.now(pytz.utc)
    tomorrow = datetime.datetime.replace(datetime.datetime.now(pytz.utc) + datetime.timedelta(days=1), hour=0, minute=0, second=3)
    to_sleep = (tomorrow-now).seconds + 10
    logger.info(f'Now is {now}.\nTomorrow will be in {to_sleep}.\nSleeping {to_sleep/60} minutes...')
    time.sleep(to_sleep)


def timestamp_log():
    return datetime.datetime.now(pytz.utc).replace(microsecond=0, tzinfo=None)




