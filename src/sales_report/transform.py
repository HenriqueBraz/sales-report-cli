import logging
from typing import Any

logger = logging.getLogger(__name__)


class Transformer:
    def __init__(self, sales: list[dict]):
        logger.info("Initializing sales transformer")
        self.sales = sales
        self._product_totals = self._calculate_product_totals()

    def _calculate_product_totals(self) -> list[dict[str, Any]]:
        logger.info("Calculating product totals")
        totals: list[dict[str, Any]] = []
        for sale in self.sales:
            product = next((p for p in totals if p["produto"] == sale["produto"]), None)
            if product:
                product["quantidade"] += int(sale["quantidade"])
                product["total_vendas"] += int(sale["quantidade"]) * float(
                    sale["preco_unitario"]
                )
            else:
                new_product = {
                    "produto": sale["produto"],
                    "quantidade": int(sale["quantidade"]),
                    "total_vendas": int(sale["quantidade"])
                    * float(sale["preco_unitario"]),
                }
                totals.append(new_product)

        return totals

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

    def most_sold_product(self) -> dict[str, Any]:
        logger.info("Retrieving most sold product")
        if not self._product_totals:
            return {}
        most_sold = max(self._product_totals, key=lambda p: p["quantidade"])
        return most_sold
