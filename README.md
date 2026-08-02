# Sales Report CLI

Simple command-line application that reads sales data from a CSV file and generates summary reports in text or JSON format.

## Requirements

- Python 3.10+

## Installation

Clone the repository and install the project:

```bash
git clone <repository-url>
cd sales-report-cli
pip install -e ".[dev]"
```

## Running

Generate a report in text format:

```bash
vendas-cli vendas_exemplo.csv
```

Generate a report in JSON format:

```bash
vendas-cli vendas_exemplo.csv -f json
```

Filter sales by date:

```bash
vendas-cli vendas_exemplo.csv --start 2025-02-01 --end 2025-02-28
```

## Running the tests

Execute all tests:

```bash
pytest -v
```

Generate the coverage report:

```bash
pytest --cov --cov-report=term-missing --cov-report=html
```

The HTML report will be available at:

```text
htmlcov/index.html
```

## Project structure

```
src/
├── extract.py
├── transform.py
├── presenter.py
└── cli.py

tests/
```

## Test Coverage

Current automated test coverage: **92%** (measured with `pytest-cov`).