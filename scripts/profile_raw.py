
import csv
import hashlib
import json
from pathlib import Path


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "894233989_32020_056_airline_delay_causes.csv"
)

OUTPUT_FILE = PROJECT_ROOT / "docs" / "profiling_results.md"


def is_missing(value: str) -> bool:
    """Return True if a CSV value is empty or contains only spaces."""
    return value.strip() == ""


def infer_type(value: str) -> str:
    """Infer a basic data type from a non-empty CSV value."""

    value = value.strip()

    try:
        int(value)
        return "integer"
    except ValueError:
        pass

    try:
        float(value)
        return "float"
    except ValueError:
        return "text"


def profile_csv(file_path: Path) -> str:
    """Profile the raw CSV without modifying the original file."""

    if not file_path.is_file():
        raise FileNotFoundError(f"Raw file not found: {file_path}")

    missing_counts = []
    type_counts = []
    duplicate_hashes = set()

    total_records = 0
    duplicate_records = 0
    malformed_records = 0
    month_invalid = 0
    month_examples = []

    with file_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.reader(csv_file, strict=True)
        header = next(reader, None)

        if not header:
            raise ValueError("CSV file is empty or has no header.")

        column_count = len(header)

        # Find the month column once before processing the records.
        month_index = next(
            (
                index
                for index, name in enumerate(header)
                if name.strip() == "month"
            ),
            None
        )

        missing_counts = [0] * column_count

        type_counts = [
            {"integer": 0, "float": 0, "text": 0}
            for _ in header
        ]

        for row in reader:
            total_records += 1

            # Detect rows with an unexpected number of fields.
            if len(row) != column_count:
                malformed_records += 1

            # Detect duplicate parsed CSV records.
            row_text = json.dumps(
                row,
                ensure_ascii=False,
                separators=(",", ":")
            )

            row_hash = hashlib.sha256(
                row_text.encode("utf-8")
            ).hexdigest()

            if row_hash in duplicate_hashes:
                duplicate_records += 1
            else:
                duplicate_hashes.add(row_hash)

            # Profile each column.
            for index in range(column_count):
                value = row[index] if index < len(row) else ""

                if is_missing(value):
                    missing_counts[index] += 1
                else:
                    value_type = infer_type(value)
                    type_counts[index][value_type] += 1

            # Validate month values when the column exists.
            if month_index is not None:
                month_value = (
                    row[month_index].strip()
                    if month_index < len(row)
                    else ""
                )

                try:
                    month_number = int(month_value)

                    if not 1 <= month_number <= 12:
                        raise ValueError

                except ValueError:
                    month_invalid += 1

                    if len(month_examples) < 5:
                        month_examples.append(
                            month_value or "<empty>"
                        )

    # Build the profiling report.
    report = []

    report.append("# Raw Dataset Profiling Results\n")
    report.append("## 1. Dataset Overview\n")
    report.append(f"- **File:** `{file_path.name}`")
    report.append(f"- **Total records:** {total_records:,}")
    report.append(f"- **Total columns:** {column_count}")
    report.append(f"- **Duplicate records:** {duplicate_records:,}")
    report.append(
        f"- **Rows with unexpected field count:** {malformed_records:,}"
    )
    report.append("")

    report.append("## 2. Column Name Issues\n")

    blank_headers = [
        str(index + 1)
        for index, name in enumerate(header)
        if name.strip() == ""
    ]

    whitespace_headers = [
        name
        for name in header
        if name != name.strip() and name.strip() != ""
    ]

    report.append(
        f"- **Empty column names:** {len(blank_headers)}"
    )
    report.append(
        f"- **Column names with extra surrounding spaces:** "
        f"{len(whitespace_headers)}"
    )

    if blank_headers:
        report.append(
            f"- Empty header positions: {', '.join(blank_headers)}"
        )

    if whitespace_headers:
        report.append(
            "- Column names with spaces: "
            + ", ".join(f"`{name}`" for name in whitespace_headers)
        )

    report.append("")

    report.append("## 3. Missing Values and Data Types\n")
    report.append(
        "| Column | Missing Values | Integer | Float | Text |"
    )
    report.append("|---|---:|---:|---:|---:|")

    for index, name in enumerate(header):
        counts = type_counts[index]

        report.append(
            f"| `{name}` | {missing_counts[index]:,} "
            f"| {counts['integer']:,} "
            f"| {counts['float']:,} "
            f"| {counts['text']:,} |"
        )

    report.append("")

    report.append("## 4. Month Value Validation\n")
    report.append(
        f"- **Invalid or missing month values:** {month_invalid:,}"
    )

    if month_examples:
        report.append(
            "- Example invalid values: "
            + ", ".join(f"`{value}`" for value in month_examples)
        )

    report.append("")

    report.append("## 5. Initial Observations\n")
    report.append(
        "- This report describes the raw dataset before cleaning."
    )
    report.append(
        "- Missing values are counted when a field is empty "
        "or contains only whitespace."
    )
    report.append(
        "- Duplicate records are identified using a SHA-256 "
        "fingerprint of each parsed CSV row."
    )
    report.append(
        "- Numeric types are inferred from the values; "
        "they are not validated against a complete data schema."
    )
    report.append("- No source data has been modified.")

    return "\n".join(report)


def main():
    report = profile_csv(RAW_FILE)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(report, encoding="utf-8")

    print("Raw data profiling completed successfully.")
    print(f"Report saved to: {OUTPUT_FILE}")
    print()
    print(report)


if __name__ == "__main__":
    main()
