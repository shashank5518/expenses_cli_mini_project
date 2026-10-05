from pathlib import Path


def validate_file_type(file_path: Path) -> None:
    if file_path.suffix.lower() != '.csv':
        raise ValueError("File must be a CSV file.")