import hashlib
import shutil
from pathlib import Path


def calculate_sha256(file_path: Path) -> str:
    """Calculate the SHA-256 checksum of a file."""

    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def preserve_raw_file(source_file: Path, raw_dir: Path) -> Path:
    """
    Copy the original source file into the raw data directory
    without modifying its contents, then verify its integrity.
    """

    source_file = Path(source_file)
    raw_dir = Path(raw_dir)

    # Validate the source file
    if not source_file.exists():
        raise FileNotFoundError(
            f"Source file was not found: {source_file}"
        )

    if not source_file.is_file():
        raise ValueError(
            f"Source path is not a file: {source_file}"
        )

    if source_file.stat().st_size == 0:
        raise ValueError("Source file is empty.")

    # Create the raw directory if it does not exist
    raw_dir.mkdir(parents=True, exist_ok=True)

    destination_file = raw_dir / source_file.name

    # Prevent copying a file onto itself
    if source_file.resolve() == destination_file.resolve():
        raise ValueError(
            "Source and destination paths must be different."
        )

    try:
        # Preserve the original file without transformation
        shutil.copy2(source_file, destination_file)

        # Verify that the copied file is identical to the source
        source_hash = calculate_sha256(source_file)
        destination_hash = calculate_sha256(destination_file)

        if source_hash != destination_hash:
            destination_file.unlink(missing_ok=True)
            raise IOError(
                "Raw file integrity check failed: SHA-256 mismatch."
            )

        return destination_file

    except OSError as error:
        raise OSError(
            f"Failed to preserve raw file: {error}"
        ) from error
