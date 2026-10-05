from pathlib import Path


def convert_to_utf8(
        file_path: Path,
        source_encoding: str,
        output_path: Path,
) -> None:
    with file_path.open(
        'r',
        encoding = source_encoding,
        newline='', 
    ) as source_file:
        content = source_file.read()

    with output_path.open(
        'w',
        encoding="utf-8",
        newline="",
    ) as output_file:
        output_file.write(content)