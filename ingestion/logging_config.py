
import logging


def setup_logger() -> logging.Logger:
    """Configure and return the pipeline logger."""

    logger = logging.getLogger("flight_ingestion")
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers
    if not logger.handlers:
        console_handler = logging.StreamHandler()

        log_format = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler.setFormatter(log_format)
        logger.addHandler(console_handler)

    return logger
