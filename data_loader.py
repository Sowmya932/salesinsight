import pandas as pd
from pathlib import Path

def load_data(file_path: str) -> pd.DataFrame:
    """Load and clean sales data."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    df = pd.read_csv(file_path)
    df['Month'] = pd.to_datetime(df['Month'])
    return df
