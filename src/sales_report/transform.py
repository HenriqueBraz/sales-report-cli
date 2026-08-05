import logging
from typing import Any
from datetime import datetime

logger = logging.getLogger(__name__)


class Transformer:
    def __init__(self, sales: list[dict]):
        logger.info("Initializing sales transformer")
        self.sales = sales
        self._product_totals = self._calculate_product_totals()

    def filter_by_date(self, start: str | None, end: str | None) -> list[dict]:
        logger.info("Filtering sales between %s and %s", start, end)
        start_date = datetime.strptime(start, "%Y-%m-%d").date() if start else None
        end_date = datetime.strptime(end, "%Y-%m-%d").date() if end else None
        filtered_sales = []
        for sale in self.sales:
            sale_date = datetime.strptime(
                sale["data"],
                "%Y-%m-%d",
            ).date()
            if start_date and sale_date < start_date:
                continue

            if end_date and sale_date > end_date:
                continue

            filtered_sales.append(sale)
        logger.info("Filtered %d of %d sales", len(filtered_sales), len(self.sales))
        return filtered_sales

    def _calculate_product_totals(self) -> list[dict[str, Any]]:
        logger.info("Calculating product totals")
        totals: dict[str, dict[str, Any]] = {}
        for sale in self.sales:
            product = sale["produto"]
            quantity = int(sale["quantidade"])
            total = quantity * float(sale["preco_unitario"])

            if product not in totals:
                totals[product] = {
                    "produto": product,
                    "quantidade": quantity,
                    "total_vendas": total,
                }
            else:
                totals[product]["quantidade"] += quantity
                totals[product]["total_vendas"] += total

        return list(totals.values())

    def total_sales_by_product(self) -> list[dict[str, Any]]:
        logger.info("Returning total sales by product")
        if not self._product_totals:
            return []
        return self._product_totals

    def total_sales_value(self) -> float:
        logger.info("Calculating total sales value")
        total = 0
        for sale in self.sales:
            total += float(sale["preco_unitario"]) * int(sale["quantidade"])
        return total

    def most_sold_product(self) -> list[dict[str, Any]]:
        logger.info("Retrieving most sold product")
        if not self._product_totals:
            return [{}]
       
        most_sold = max(self._product_totals, key=lambda p: p["quantidade"])
        most_solds = [most_sold]
        for product in self._product_totals:
            if product["quantidade"] == most_sold["quantidade"] and most_sold['produto'] != product['produto']:
                most_solds.append(product)
                break

        return most_solds
