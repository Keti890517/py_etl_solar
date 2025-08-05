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

py_etl_pipeline/
├── output/
│ ├── daily_csv/ # Cleaned sensor data for each date
│ └── aggregates/ # Daily production totals
├── src/
│ ├── etl.py # Main ETL logic
│ ├── validators.py # Data validation functions
│ ├── utils.py # File and datetime helpers
│ └── config.py # Constants (e.g. valid time window)
├── main.py # CLI entrypoint
├── .gitignore
├── requirements.txt
└── README.md