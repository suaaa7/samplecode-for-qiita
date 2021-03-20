from io import StringIO
from typing import Optional

import pandas as pd


def json_str_to_df(json_str: str) -> Optional[pd.DataFrame]:
    try:
        return pd.read_json(path_or_buf=StringIO(json_str), orient='records')
    except ValueError:
        return None
