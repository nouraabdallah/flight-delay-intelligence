
import sys
import time

from ingestion.config import SOURCE_FILE, RAW_DIR
from ingestion.source import validate_source, count_records
from ingestion.storage import preserve_raw_file
from ingestion.logging_config import setup_logger


def main() -> int:
    """Run the complete raw data ingestion pipeline."""

    logger = setup_logger()
    start_time = time.perf_counter()

    logger.info("Starting Flight Delay Ingestion Pipeline")

    try:
        # Step 1: Validate the source file
        logger.info("Checking source file: %s", SOURCE_FILE)
        validated_file = validate_source(SOURCE_FILE)
        logger.info("Source status: AVAILABLE")

        # Step 2: Count CSV records
        total_records = count_records(validated_file)
        logger.info("Total records fetched: %d", total_records)

        # Step 3: Preserve the original file
        logger.info("Starting raw data preservation")
        raw_file = preserve_raw_file(validated_file, RAW_DIR)

        logger.info("Raw file successfully saved: %s", raw_file)
        logger.info(
            "Raw file size: %d bytes",
            raw_file.stat().st_size
        )

        # Pipeline completed successfully
        elapsed_time = time.perf_counter() - start_time
        logger.info("Pipeline status: SUCCESS")
        logger.info("Execution time: %.2f seconds", elapsed_time)

        return 0

    except Exception:
        elapsed_time = time.perf_counter() - start_time
        logger.exception("Pipeline status: FAILED")
        logger.info("Execution time before failure: %.2f seconds", elapsed_time)

        return 1


if __name__ == "__main__":
    sys.exit(main())
