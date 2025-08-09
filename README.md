# Sensor ETL Pipeline

## Overview

This project implements a lightweight and reproducible ETL pipeline in Python to process solar panel sensor data provided in JSON format. It demonstrates:

- Clean and readable Python coding practices
- Maintainable, modular project structure suitable for teamwork
- Version-controlled development using Git
- Thoughtful data validation
- Support for reproducible, CI/CD-ready execution

---

## 🔧 Features

- ✅ Reads all JSON sensor files for a specified date
- ✅ Validates data:
  - Drops invalid timestamps (outside March 2025)
  - Overrides non-zero night-time production with 0
  - Replaces anomalous readings (> 3.0) with the previous valid value
- ✅ Saves cleaned daily data to CSV files
- ✅ Aggregates total daily production into a summary CSV

---

## 📁 Project Structure

project_root/
│
├── main.py                 # script entry point: argument parsing and orchestration
├── src/
│   ├── __init__.py
│   ├── file_utils.py       # file-related utilities (list files, validate filenames)
│   ├── data_processing.py  # data loading, validation, cleaning logic
│   ├── aggregation.py      # aggregation logic
│   └── utils.py            # misc utilities (e.g. windows_to_wsl_path)
└── output/
    ├── daily_csv/
    └── aggregates/

---

## Running the script

Run the ETL pipeline from the command line as follows:

python main.py --data-dir "<PATH_TO_JSON_FILES>" [--input-date YYYY-MM-DD]

--data-dir (required): Windows-style path to the folder containing JSON sensor data files.

--input-date (optional): Specific date to process in YYYY-MM-DD format. If omitted, all data from March 2025 will be processed.

Example:

python main.py --data-dir "C:\Users\User\Downloads\jsons" --input-date 2025-03-10
Processed daily CSVs will be saved in output/daily_csv/ and the aggregated summary in output/aggregates/aggregates.csv.

## LLM Tool Usage

During this project LLM was used to propose a project structure and generate README, as well as to review & spar during writing the code, as a sparring partner or reviewer was not available, as it would be during a production task. I aimed to implement the outline and structure and use LLM to review.