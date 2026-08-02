import json
from sales_report.presenter import Presenter


def test_to_text(report_data):
    presenter = Presenter(**report_data)

    report = presenter.to_text()

    assert "Sales Report" in report
    assert "Camiseta" in report
    assert "Calça" in report
    assert "399.40" in report
    assert "Most Sold Product" in report


def test_to_json(report_data):
    presenter = Presenter(**report_data)

    report_json = presenter.to_json()

    report_dict = json.loads(report_json)

    assert report_dict == report_data
