import csv
from datetime import date
from decimal import Decimal
from pathlib import Path

from src.models import Expense


def load_expenses(file_path: Path) -> list[Expense]:
    expenses = []
    with file_path.open(newline = '', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expense = Expense(
                date = date.fromisoformat(row["date"]),
                description = row["description"],
                category = row["category"],
                amount = Decimal(row["amount"]),
                payment_method = row["payment_method"],
            )

            expenses.append(expense)
    return expenses