
import csv
from pathlib import Path

from ingestion.config import SOURCE_FILE


def validate_source(source_file: Path = SOURCE_FILE) -> Path:
    """Check that the source CSV exists and is not empty."""

    if not source_file.exists():
        raise FileNotFoundError(
            f"Source file was not found: {source_file}"
        )

    if not source_file.is_file():
        raise ValueError(
            f"Source path is not a file: {source_file}"
        )

    if source_file.stat().st_size == 0:
        raise ValueError(
            f"Source file is empty: {source_file}"
        )

    return source_file


def count_records(source_file: Path = SOURCE_FILE) -> int:
    """Count CSV data records without counting the header."""

    validated_file = validate_source(source_file)

    try:
        with validated_file.open(
            mode="r",
            encoding="utf-8-sig",
            newline=""
        ) as csv_file:

            reader = csv.reader(csv_file, strict=True)

            # Skip the header row
            header = next(reader, None)

            if header is None:
                raise ValueError("CSV file has no header.")

            # Count all data records
            total_records = sum(1 for row in reader)

            return total_records

    except UnicodeDecodeError as error:
        raise ValueError(
            "Could not decode the CSV file. Check its encoding."
        ) from error

    except csv.Error as error:
        raise ValueError(
            f"Invalid CSV format: {error}"
        ) from error

    except OSError as error:
        raise OSError(
            f"Could not read source file: {error}"
        ) from error
