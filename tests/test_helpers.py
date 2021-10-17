from utils.errors import TrainingTypeError
import pytest
import utils.helpers as hlp

def test_open_sql_file():
    query = hlp.open_sql_file(filename='test_query')
    assert isinstance(query, str)
    assert query == 'SELECT TEST QUERY FROM TEST'


def test_validate_training_type():
    with pytest.raises(TrainingTypeError):
        hlp.validate_training_type('hammer throw')
    for training_type in ['weights','run', 'swim','bike','utility']:
        assert hlp.validate_training_type(training_type)
    
def test_training_id():
    used_suffixes = [x for x in range(100)]
    training_id = hlp.training_id(
        block=1,
        week=1,
        training_type='run',
        integer_suffixs=used_suffixes
    )
    assert training_id == 'B1W1R100'