import pytest
import core.utils.helpers as hlp


def test_open_sql_file():
    query = hlp.open_sql_file(filename='test_query')
    assert isinstance(query, str)
    assert query == 'SELECT TEST QUERY FROM TEST'
