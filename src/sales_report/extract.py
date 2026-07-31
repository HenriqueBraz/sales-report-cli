import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class Extractor:

     def __init__(self, file: Path):
        self.file = file


     
     def csv_extract(self) -> list[dict]:
         logger.info(f"Reading CSV file: {self.file}")
         try:
            with open(self.file, mode='r', encoding='latin1') as file: 
                  reader = csv.DictReader(file)
                  sales = list(reader)
            logger.info(f"Loaded {len(sales)} sales")
            return sales
         except FileNotFoundError:
            logger.error(f"File not found: {self.file}")
         except Exception as e:
            logger.error(f"An error occurred while reading the CSV file: {e}")   
         