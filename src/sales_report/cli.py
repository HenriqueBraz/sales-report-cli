import argparse
import logging
from pathlib import Path
from .extract import Extractor
from .transform import Transformer
from .presenter import Presenter

logger = logging.getLogger(__name__)


def main():

    parser = argparse.ArgumentParser(
        prog="sales_report", description=" a advanced sales report generator"
    )
    parser.add_argument("file", type=Path, help="Path to file containing sales data")
    parser.add_argument(
        "-f",
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format for the report, either 'text' or 'json', default is 'text'",
    )
    parser.add_argument("-s", "--start", type=str, help="Start date (YYYY-MM-DD)")
    parser.add_argument("-e", "--end", type=str, help="End date (YYYY-MM-DD)")
    args = parser.parse_args()
    file = Path(args.file)

    extractor = Extractor(file)
    file_type = file.name.split(".")[-1].lower()
    logger.info(f"Extracting sales data from {file.name}")
    if file_type != "csv":
        logger.error(f"Unsupported file type: {file_type}")
        raise ValueError

    sales_data = extractor.csv_extract()
    transformer = Transformer(sales_data)

    if args.start or args.end:
        sales_data = transformer.filter_by_date(start=args.start, end=args.end)
        transformer = Transformer(sales_data)

    total_sales_by_product = transformer.total_sales_by_product()

    total_sales_value = transformer.total_sales_value()

    most_sold_product = transformer.most_sold_product()

    presenter = Presenter(
        total_sales_by_product=total_sales_by_product,
        total_sales_value=total_sales_value,
        most_sold_product=most_sold_product,
    )

    if args.format == "text":
        print(presenter.to_text())

    elif args.format == "json":
        print(presenter.to_json())


if __name__ == "__main__":
    try:
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        main()

    except Exception as e:
        logger.exception(f"Application terminated unexpectedly: {e}")
