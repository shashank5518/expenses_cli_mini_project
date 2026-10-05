from pathlib import Path
import chardet

def validate_file_exists(file_path: Path) -> None:
    if not file_path.is_file():
        raise FileNotFoundError(
            f"File does not exist: {file_path}"
        )

def validate_file_type(file_path: Path) -> None:
    if file_path.suffix.lower() != '.csv':
        raise ValueError("File must be a CSV file.")

def detect_encoding(file_path: Path) -> tuple[str, float]:
    with file_path.open('rb') as file:
        raw_data = file.read()

    result = chardet.detect(raw_data)
    encoding = result["encoding"]
    confidence = result["confidence"]

    if encoding is None:
        raise ValueError(
            f"Could not determine encoding for: {file_path}"
        )
    return encoding, confidence

def is_utf8_encoding(encoding: str) -> bool:
    return encoding.lower().replace("-", "") == "utf8"