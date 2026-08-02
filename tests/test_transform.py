import pytest
from sales_report.transform import Transformer


def test_total_sales_by_product(sales):
    transformer = Transformer(sales)
    result = transformer.total_sales_by_product()
    expected = [
        {
            "produto": "Camiseta",
            "quantidade": 4,
            "total_vendas": 199.6,
        },
        {
            "produto": "Calça",
            "quantidade": 2,
            "total_vendas": 199.8,
        },
        {
            "produto": "Tênis",
            "quantidade": 1,
            "total_vendas": 199.9,
        },
    ]

    assert result == expected


def test_total_sales_value(sales):
    transformer = Transformer(sales)
    result = transformer.total_sales_value()
    expected = 599.3

    assert result == pytest.approx(expected)


def test_most_sold_product(sales):
    transformer = Transformer(sales)

    result = transformer.most_sold_product()

    expected = {
        "produto": "Camiseta",
        "quantidade": 4,
        "total_vendas": 199.6,
    }

    assert result == expected


def test_total_sales_by_product_empty():
    transformer = Transformer([])

    result = transformer.total_sales_by_product()

    assert result == []


def test_most_sold_product_empty():
    transformer = Transformer([])

    result = transformer.most_sold_product()

    assert result == {}


def test_total_sales_value_empty():
    transformer = Transformer([])

    assert transformer.total_sales_value() == 0


def test_filter_by_date(sales):
    transformer = Transformer(sales)

    result = transformer.filter_by_date(start="2025-02-01", end="2025-03-31")

    expected = [
        {
            "produto": "Calça",
            "quantidade": "2",
            "preco_unitario": "99.9",
            "data": "2025-02-15",
        },
        {
            "produto": "Camiseta",
            "quantidade": "1",
            "preco_unitario": "49.9",
            "data": "2025-03-20",
        },
    ]

    assert result == expected
