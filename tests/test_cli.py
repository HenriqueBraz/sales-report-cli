from sales_report.cli import main
import json
import pytest


def test_main_text(tmp_path, capsys):
    csv_file = tmp_path / "sales.csv"

    csv_file.write_text(
        """produto,quantidade,preco_unitario,data
Camiseta,3,49.9,2025-01-10
Calça,2,99.9,2025-02-15
""",
        encoding="utf-8",
    )

    main([str(csv_file)])

    captured = capsys.readouterr()

    assert "Sales Report" in captured.out
    assert "Camiseta" in captured.out
    assert "Calça" in captured.out


def test_main_json(tmp_path, capsys):
    csv_file = tmp_path / "sales.csv"

    csv_file.write_text(
        """produto,quantidade,preco_unitario,data
Camiseta,3,49.9,2025-01-10
""",
        encoding="utf-8",
    )

    main([str(csv_file), "-f", "json"])

    captured = capsys.readouterr()

    report = json.loads(captured.out)

    assert report["total_sales_value"] == 149.7


def test_main_invalid_extension(tmp_path):
    txt_file = tmp_path / "sales.txt"

    txt_file.write_text("teste")

    with pytest.raises(ValueError):
        main([str(txt_file)])


def test_main_filter_date(tmp_path, capsys):
    csv_file = tmp_path / "sales.csv"

    csv_file.write_text(
        """produto,quantidade,preco_unitario,data
Camiseta,3,49.9,2025-01-10
Calça,2,99.9,2025-02-15
""",
        encoding="utf-8",
    )

    main(
        [
            str(csv_file),
            "--start",
            "2025-02-01",
            "--end",
            "2025-02-28",
        ]
    )

    captured = capsys.readouterr()

    assert "Calça" in captured.out
    assert "Camiseta" not in captured.out
