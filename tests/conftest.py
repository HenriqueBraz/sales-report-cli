import pytest


@pytest.fixture
def sales():
    return [
        {
            "produto": "Camiseta",
            "quantidade": "3",
            "preco_unitario": "49.9",
            "data": "2025-01-10",
        },
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
        {
            "produto": "Tênis",
            "quantidade": "1",
            "preco_unitario": "199.9",
            "data": "2025-04-02",
        },
    ]


@pytest.fixture
def report_data():
    return {
        "total_sales_by_product": [
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
        ],
        "total_sales_value": 399.4,
        "most_sold_product": {
            "produto": "Camiseta",
            "quantidade": 4,
            "total_vendas": 199.6,
        },
    }
