import pandas as pd
from typing import Union
from pathlib import Path


class CsvLoader:
    def __init__(self, data: pd.DataFrame):
        self.input = data

    def load_to_csv(self, save_directory: Union[str, Path], filename: str):
        if isinstance(save_directory, str):
            save_directory = Path(save_directory)
        full_name = save_directory.joinpath(filename).with_suffix('.csv')
        self.input.to_csv(
            path_or_buf=full_name,
            header=True,
            index=False,
            encoding='utf-8-sig',
            date_format='%Y-%m-%d'
        )
