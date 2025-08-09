import pandas as pd

def load_and_validate_json(file_path):
    """
    Load JSON file and convert to DataFrame with proper dtypes.
    Raises exception if JSON invalid or missing keys.
    """
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    df = pd.DataFrame([data])

    # Convert types
    df['measurement_ts'] = pd.to_datetime(df['measurement_ts'], errors='coerce')
    df['production_rate'] = pd.to_numeric(df['production_rate'], errors='coerce')

    return df

def validate_timestamp(df, year=2025, month=3):
    """
    Check all timestamps are in given year/month.
    """
    return ((df['measurement_ts'].dt.year == year) & (df['measurement_ts'].dt.month == month)).all()

def correct_production_rate(df):
    """
    Implements:
    - Non-zero production outside sunlight hours set to zero.
    - Values > 3 replaced by previous reading.
    """
    outside_sunlight = ~df['measurement_ts'].dt.hour.between(6, 17)
    if df.loc[outside_sunlight & (df['production_rate'] > 0)].shape[0] > 0:
        print(f"[INFO] Non-zero production outside sunlight — values overridden to 0")
        df.loc[outside_sunlight, 'production_rate'] = 0.0

    high_values = df['production_rate'] > 3.0
    if high_values.any():
        print(f"[WARNING] High production values (>3.0) — replaced with previous reading")
        df.loc[high_values, 'production_rate'] = df['production_rate'].shift(1)

    return df