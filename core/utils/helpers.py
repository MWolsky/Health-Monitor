import core.utils.directories as hlp
import json
import datetime


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

