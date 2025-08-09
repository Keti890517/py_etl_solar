import os

def list_valid_json_files(data_dir, parts_count=3):
    """
    List JSON files in a directory with exactly `parts_count` parts split by '_'.
    """
    return [
        f for f in os.listdir(data_dir)
        if f.endswith('.json') and len(f.split('_')) == parts_count
    ]

def sort_files_chronologically(files):
    """
    Sort files by the timestamp in the middle part of the filename.
    """
    return sorted(files, key=lambda f: f.split('_')[1])