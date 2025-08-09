import sys
import os
from datetime import datetime
from src.utils import windows_to_wsl_path
from src.file_utils import list_valid_json_files, sort_files_chronologically
from src.data_processing import load_and_validate_json, validate_timestamp, correct_production_rate
from src.aggregation import aggregate_production_rates

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=str, required=True, help="Path to data folder (Windows style)")
    parser.add_argument('--input-date', type=str, help="Date for processing (YYYY-MM-DD), if not provided processes full 2025 March.")
    return parser.parse_args()

def main():
    cwd = os.getcwd()
    args = parse_args()
    data_dir = windows_to_wsl_path(args.data_dir)
    print(data_dir)
    if not os.path.exists(data_dir):
        print(f"Path not found: {data_dir}")
        sys.exit(1)

    # Validate input date format upfront
    if args.input_date:
        try:
            datetime.strptime(args.input_date, "%Y-%m-%d")
        except ValueError:
            print(f"Error: --input-date '{args.input_date}' is not a valid date in YYYY-MM-DD format.")
            sys.exit(1)

    json_files = list_valid_json_files(data_dir)
    json_files = sort_files_chronologically(json_files)

    for file in json_files:
        full_path = os.path.join(data_dir, file)
        title_timestamp = file.split('_')[1]

        should_open = False
        if args.input_date:
            input_date = args.input_date.replace('-', '')
            if input_date == title_timestamp[:8]:
                should_open = True
        else:
            if title_timestamp[:6] == "202503":
                should_open = True

        if should_open:
            try:
                df = load_and_validate_json(full_path)
            except Exception as e:
                print(f"Skipping file {file} — {e}")
                continue

            if not validate_timestamp(df):
                print(f"Skipping file {file} — incorrect timestamp")
                continue

            df = correct_production_rate(df)

            file_name_csv = f"{title_timestamp[:12]}.csv"
            path = os.path.join(cwd, "output", "daily_csv", file_name_csv)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            df.to_csv(path, index=False)
            print(f"Processed data saved to: {path}")

    aggregated_df = aggregate_production_rates(os.path.join(cwd, "output", "daily_csv"))
    output_path = os.path.join(cwd, "output", "aggregates", "aggregates.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    aggregated_df.to_csv(output_path, index=False)
    print(f"Aggregated CSV saved to: {output_path}")

if __name__ == "__main__":
    main()