import pandas as pd
from typing import List, Union


def deduplicate_input_df(
        input_df: pd.DataFrame,
        table: pd.DataFrame,
        input_df_fields: Union[str, List[str]],
        table_fields: Union[str, List[str]]):

    if isinstance(input_df_fields, list) and isinstance(table_fields, str):
        raise TypeError('Fields to deduplicate on need to be either both str, or both list of str.')
    elif isinstance(input_df_fields, str) and isinstance(table_fields, list):
        raise TypeError('Fields to deduplicate on need to be either both str, or both list of str.')
    elif isinstance(input_df_fields, str) and isinstance(table_fields, str):
        deduplicated = input_df[~input_df[input_df_fields].isin(table[table_fields])]
    else:
        input_df['temp_indicator'] = input_df[input_df_fields].apply(lambda x: ','.join(x.values.astype(str)), axis=1)
        table['temp_indicator'] = table[table_fields].apply(lambda x: ','.join(x.values.astype(str)), axis=1)
        deduplicated = input_df[~input_df['temp_indicator'].isin(table['temp_indicator'])]
        deduplicated.drop(columns=['temp_indicator'], inplace=True)
    return deduplicated
