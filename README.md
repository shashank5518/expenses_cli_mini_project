# Expense Analyzer

A simple Python expense analysis project that loads expense data from a CSV file and calculates total spending, spending by category, spending by month, and filtered expense totals.

The project was built to practice Python data processing, modular programming, filtering, aggregation, type hints, and handling financial values with `Decimal`.

## Features

- Load expense data from CSV
- Represent expenses using a Python dataclass
- Calculate total expenses
- Calculate expenses by category
- Calculate expenses by month
- Filter expenses by category
- Filter expenses by month
- Combine filters to answer more specific questions
- Use `Decimal` for monetary calculations
- Use type hints throughout the project

## Dataset

The project uses `expenses_clean.csv` as its input dataset.

The CSV contains the following fields:

```text
date
description
category
amount
payment_method
```

Example:

```csv
date,description,category,amount,payment_method
2026-01-01,Vegetable market,Groceries,1670.18,Credit Card
2026-01-01,Monthly rent,Rent,18000.00,Bank Transfer
2026-01-03,Movie tickets,Entertainment,1938.30,Credit Card
```

## Project Structure

```text
expenses_cli/
│
├── data/
│   └── expenses_clean.csv
│
├── src/
│   ├── analytics.py
│   ├── filters.py
│   ├── loader.py
│   └── models.py
│
├── main.py
├── pyproject.toml
└── README.md
```

## How It Works

The application follows a simple data-processing flow:

```text
expenses_clean.csv
        ↓
    loader.py
        ↓
  Expense objects
        ↓
 ┌──────┴───────┐
 ↓              ↓
filters.py   analytics.py
 ↓              ↓
Filtered      Aggregated
expenses      results
        ↓
      main.py
        ↓
      Output
```

### `models.py`

Defines the `Expense` dataclass used to represent an individual expense.

Each expense contains:

- Date
- Description
- Category
- Amount
- Payment method

The amount is stored as a `Decimal` rather than a floating-point number.

### `loader.py`

Reads the CSV using Python's `csv.DictReader` and converts each row into an `Expense` object.

Dates are converted to `datetime.date` and monetary values are converted to `Decimal`.

### `analytics.py`

Contains the main aggregation functions:

```python
total_expenses(expenses)
total_by_category(expenses)
total_by_month(expenses)
```

`total_by_category()` groups expenses by category and sums their amounts, while `total_by_month()` groups expenses using the `YYYY-MM` representation of their dates.

### `filters.py`

Contains filtering functions for:

```python
filter_by_category(expenses, category)
filter_by_month(expenses, year, month)
```

Category filtering is case-insensitive, while month filtering matches the year and month of each expense.

### `main.py`

Acts as the entry point for the application.

It loads the expense data, calculates overall/category/monthly totals, and demonstrates filtering functionality.

## Example Output

Using the current dataset:

```text
Loaded 367 expenses
Total expenses: 583330.86

Rent: 162000.00
Groceries: 95248.05
Shopping: 86965.33
Dining: 62621.42
Education: 45171.69
Transport: 40060.72
Utilities: 29478.00
Health: 28503.11
Entertainment: 26370.54
Subscriptions: 6912.00
```

The program can also calculate filtered results, such as total entertainment expenses or health expenses for June 2026.

## Requirements

- Python 3.13
- No external data-processing library is required for the application itself.

The project is configured for Python 3.13 and uses Ruff, Black, MyPy, and Pytest configuration through `pyproject.toml`.

## Running the Project

Place the CSV file in the expected `data` directory:

```text
data/
└── expenses_clean.csv
```

Then run:

```bash
python main.py
```

The current `main.py` expects the project to be run from the configured project directory and loads the CSV from:

```text
data/expenses_clean.csv
```

## Code Quality

The project is configured with:

### Black

Line length:

```text
88 characters
```

### Ruff

Configured for Python 3.13 with rules covering:

- pycodestyle
- Pyflakes
- import sorting
- pyupgrade
- bugbear
- simplification
- comprehensions
- return statements

### MyPy

Configured with several type-checking safeguards, including:

- Untyped function definition checks
- Unreachable code warnings
- Redundant cast warnings
- Strict equality checks
- Python 3.13 target

These configurations are defined in `pyproject.toml`.

## What I Learned

This project focuses on practicing:

- Python file handling
- CSV processing
- Dataclasses
- Type hints
- `pathlib`
- `datetime`
- `Decimal`
- `defaultdict`
- List comprehensions
- Dictionary aggregation
- Sorting
- Filtering collections
- Modular Python project structure
- Separating data loading, filtering, and analytics logic

## Future Improvements

Potential future iterations could include:

- `argparse`-based command-line arguments
- Date-range filtering
- Payment-method filtering
- Minimum/maximum amount filters
- Exporting analysis results
- Unit tests with Pytest
- Pandas implementation
- PostgreSQL storage
- FastAPI API
- ETL pipeline
- Dockerization

These are future extensions rather than features of the current version.