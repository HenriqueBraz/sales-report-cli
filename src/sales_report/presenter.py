import json
import logging

logger = logging.getLogger(__name__)


class Presenter:
    def __init__(
        self,
        total_sales_by_product: list[dict],
        total_sales_value: float,
        most_sold_product: dict,
    ):

        self.total_sales_by_product = total_sales_by_product
        self.total_sales_value = total_sales_value
        self.most_sold_product = most_sold_product

    def to_text(self) -> str:
        logger.info("Generating text report")
        report = "============\n\n"
        report += "Sales Report\n"
        report += "============\n\n"
        report += "Total Sales by Product:\n"
        for product in self.total_sales_by_product:
            report += f"- {product['produto']}: ${product['total_vendas']:.2f}\n"
        report += f"\nTotal Sales Value: ${self.total_sales_value:.2f}\n"
        report += f"Most Sold Product: {self.most_sold_product['produto']} ({self.most_sold_product['quantidade']} units)\n"
        return report

    def to_json(self) -> str:
        logger.info("Generating JSON report")
        report = {
            "total_sales_by_product": self.total_sales_by_product,
            "total_sales_value": self.total_sales_value,
            "most_sold_product": self.most_sold_product,
        }
        return json.dumps(
            report,
            indent=4,
            ensure_ascii=False,
        )
