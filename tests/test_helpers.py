import pytest
import core.utils.helpers as hlp
from datetime import datetime
from freezegun import freeze_time
import pytz


def test_open_sql_file():
    query = hlp.open_sql_file(filename='test_query')
    assert isinstance(query, str)
    assert query == 'SELECT TEST QUERY FROM TEST'


@freeze_time(datetime(2021, 12, 6))
def test_daily_timestamp_counter(daily_timestamps):
    limit = 10
    timestamp_list = [datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in daily_timestamps]
    assert hlp.daily_timestamp_counter(timestamp_list, limit)[0] is True
    timestamp_list.append(datetime.now(tz=pytz.utc).replace(microsecond=0, tzinfo=None))
    assert hlp.daily_timestamp_counter(timestamp_list, limit)[0] is True
    timestamp_list.append(datetime(2021, 12, 5, tzinfo=None))
    assert hlp.daily_timestamp_counter(timestamp_list, limit)[0] is True
    timestamp_list.append(datetime.now(tz=pytz.utc).replace(microsecond=0, tzinfo=None))
    assert hlp.daily_timestamp_counter(timestamp_list, limit)[0] is False


@freeze_time(datetime(2021, 12, 6, 21, 29, 54))
def test_quarter_hour_timestamp_counter(quarter_hour_timestamps):
    limit = 10
    timestamp_list = [datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in quarter_hour_timestamps]
    assert hlp.quarter_an_hour_timestamp_counter(timestamp_list, limit)[0] is True
    timestamp_list.append(datetime(2021, 12, 6, 21, 0, 0, tzinfo=None))
    assert hlp.quarter_an_hour_timestamp_counter(timestamp_list, limit)[0] is True
    timestamp_list.append(datetime(2021, 12, 6, 21, 29, 55, tzinfo=None))
    assert hlp.quarter_an_hour_timestamp_counter(timestamp_list, limit)[0] is True
    timestamp_list.append(datetime(2021, 12, 6, 21, 29, 56, tzinfo=None))
    assert hlp.quarter_an_hour_timestamp_counter(timestamp_list, limit)[0] is True
    timestamp_list.append(datetime(2021, 12, 6, 21, 29, 56, tzinfo=None))
    assert hlp.quarter_an_hour_timestamp_counter(timestamp_list, limit)[0] is True
    timestamp_list.append(datetime(2021, 12, 6, 21, 29, 56, tzinfo=None))
    assert hlp.quarter_an_hour_timestamp_counter(timestamp_list, limit)[0] is True
    timestamp_list.append(datetime(2021, 12, 6, 21, 29, 56, tzinfo=None))
    assert hlp.quarter_an_hour_timestamp_counter(timestamp_list, limit)[0] is False
    timestamp_list.append(datetime(2021, 12, 6, 21, 29, 56, tzinfo=None))
    assert hlp.quarter_an_hour_timestamp_counter(timestamp_list, limit)[0] is False
