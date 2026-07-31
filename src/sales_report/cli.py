import argparse
import logging
from pathlib import Path

from .extract import Extractor
from .transform import Transformer


def main():

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        prog="sales_report", description=" a advanced sales report generator"
    )

    parser.add_argument("file", type=Path, help="Path to file containing sales data")
    args = parser.parse_args()
    file = Path(args.file)

    extractor = Extractor(file)
    file_type = file.name.split(".")[-1].lower()
    logger.info(f"Extracting sales data from {file.name}")
    if file_type == "csv":
        sales_data = extractor.csv_extract()
    else:
        logger.error(f"Unsupported file type: {file_type}")

    print()
    print("Sales data:")
    print(sales_data)
    print()

    transformer = Transformer(sales_data)

    print("Total sales by product:")
    total_sales_by_product = transformer.total_sales_by_product()
    print(total_sales_by_product)

    print("Total sales value:")
    total_sales_value = transformer.total_sales_value()
    print(total_sales_value)

    print("Most sold product:")
    most_sold_product = transformer.most_sold_product()
    print(most_sold_product)


if __name__ == "__main__":
    main()
