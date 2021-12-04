import pandas as pd
import pytest
from core.transformers.data_processing import deduplicate_input_df


def test_deduplicate_input_df_by_list(input_dataframe, target_dataframe):
    deduplicated = deduplicate_input_df(
        input_dataframe,
        target_dataframe,
        ['column1', 'column2', 'column3'],
        ['col1', 'col2', 'col3']
    )
    joined = pd.concat([target_dataframe, deduplicated])
    assert len(input_dataframe) != len(deduplicated)
    assert joined.duplicated().sum() == 0


def test_deduplicate_input_df_by_one_field(input_dataframe, target_dataframe):
    deduplicated = deduplicate_input_df(
        input_dataframe,
        target_dataframe,
        'column1',
        'col1'
    )
    joined = pd.concat([target_dataframe, deduplicated])
    assert len(input_dataframe) != len(deduplicated)
    assert joined.duplicated().sum() == 0