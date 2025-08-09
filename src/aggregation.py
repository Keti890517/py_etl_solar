import pandas as pd
from collections import defaultdict
import glob
import os

def aggregate_production_rates(daily_csv_dir):
    """
    Read daily CSVs, sum production_rate per date and return aggregated DataFrame.
    """
    daily_files_path = os.path.join(daily_csv_dir, "*.csv")
    production_totals = defaultdict(float)

    for file in glob.glob(daily_files_path):
        df = pd.read_csv(file, usecols=["measurement_ts", "production_rate"])
        df["measurement_ts"] = pd.to_datetime(df["measurement_ts"], errors="coerce")
        df = df.dropna(subset=["measurement_ts"])

        for date, prod in zip(df["measurement_ts"].dt.date, df["production_rate"]):
            if pd.notna(date) and pd.notna(prod):
                production_totals[date] += prod

    aggregated_df = pd.DataFrame(
        list(production_totals.items()), columns=["date", "production_rate"]
    ).sort_values("date")

    return aggregated_df