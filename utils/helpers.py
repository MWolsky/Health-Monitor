import utils.directories as hlp
import config.constants as const
import utils.errors as err
from datetime import datetime


def open_sql_file(filename: str) -> str:
    fullname = filename + '.sql'
    with open (hlp.sqlcommands_dir().joinpath(fullname)) as file:
        f = file.read()
        return f


def validate_training_type(training_type: str):
    if training_type in const.training_types:
        return True
    else:
        raise err.TrainingTypeError(training_type) 

def training_id(block: int, week: int, training_type: str, integer_suffixs: list) -> str:
    if validate_training_type(training_type):
        block_part = f'B{block}'
        week_part = f'W{week}'
        type_part = training_type[0].upper()
        suffix_part = max(integer_suffixs) + 1
    training_id = f'{block_part}{week_part}{type_part}{suffix_part}'

    return training_id
