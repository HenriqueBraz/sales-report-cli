import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class Extractor:
    def __init__(self, file: Path):
        self.file = file

    def csv_extract(self) -> list[dict]:
        try:
            logger.info(f"Reading CSV file: {self.file}")
            for encoding in ("utf-8", "latin-1", "cp1252"):
                try:
                    with open(self.file, mode="r", encoding=encoding) as file:
                        reader = csv.DictReader(file)
                        sales = list(reader)

                    logger.info(
                        f"Loaded {len(sales)} sales using '{encoding}' encoding"
                    )
                    return sales

                except UnicodeDecodeError:
                    logger.warning(
                        f"Failed to decode with '{encoding}'. Trying next encoding..."
                    )

        except FileNotFoundError:
            logger.error(f"File not found: {self.file}")
            raise

        except Exception:
            logger.exception("Unexpected error while reading CSV file")
            raise

        logger.error("Unable to decode CSV file with supported encodings.")
