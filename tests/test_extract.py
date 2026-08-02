from pathlib import Path
import pytest
from sales_report.extract import Extractor


def test_csv_extract(tmp_path):

    csv_file = tmp_path / "sales.csv"
    csv_file.write_text(
        """produto,quantidade,preco_unitario,data
Camiseta,3,49.9,2025-01-10
Calça,2,99.9,2025-02-15
""",
        encoding="utf-8",
    )
    extractor = Extractor(csv_file)
    result = extractor.csv_extract()
    expected = [
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
    ]

    assert result == expected


def test_csv_file_not_found():
    extractor = Extractor(Path("non_existent_file.csv"))
    with pytest.raises(FileNotFoundError):
        extractor.csv_extract()


def test_latin1_encoding(tmp_path):
    csv_file = tmp_path / "sales_latin1.csv"
    csv_file.write_text(
        """produto,quantidade,preco_unitario,data
Tênis,3,49.9,2025-01-10""",
        encoding="latin-1",
    )
    extractor = Extractor(csv_file)
    result = extractor.csv_extract()
    expected = [
        {
            "produto": "Tênis",
            "quantidade": "3",
            "preco_unitario": "49.9",
            "data": "2025-01-10",
        }
    ]

    assert result == expected
