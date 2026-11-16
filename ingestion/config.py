import os
from pathlib import Path


# Get the main project directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent


# Define the original CSV file location
SOURCE_FILE = Path(
    os.getenv(
        "SOURCE_FILE",
        PROJECT_ROOT / "data" / "source" /
        "894233989_32020_056_airline_delay_causes.csv"
    )
)


# Define the raw data storage directory
RAW_DIR = Path(
    os.getenv(
        "RAW_DIR",
        PROJECT_ROOT / "data" / "raw"
    )
)
