import pandas as pd
from pathlib import Path

class DataHandler:
    @staticmethod
    def load_csv(path: str) -> pd.DataFrame:
        df = pd.read_csv(path, index_col=0, parse_dates=True)
        if 'Close' not in df.columns:
            raise ValueError("CSV must contain 'Close' column")
        return df.sort_index()
