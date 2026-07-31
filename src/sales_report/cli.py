import argparse
import logging
from pathlib import Path

from .extract import Extractor


def main():
    

    logging.basicConfig(level=logging.INFO, 
                        format="%(asctime)s - %(levelname)s - %(message)s")


    logger = logging.getLogger(__name__)


    parser = argparse.ArgumentParser(
                        prog='sales_report',
                        description=' a advanced sales report generator')

    parser.add_argument('file', type=Path, help='Path to file containing sales data')
    args = parser.parse_args()
    file = Path(args.file)


    extractor = Extractor(file)
    file_type = file.name.split('.')[-1].lower()
    logger.info(f"Extracting sales data from {file.name}")
    if file_type == 'csv':
        sales_data = extractor.csv_extract()
    else:
        logger.error(f"Unsupported file type: {file_type}")

    


    print(sales_data)



if __name__ == "__main__":
    main()