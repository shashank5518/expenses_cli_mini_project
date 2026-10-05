import os
from pathlib import Path

from src.analytics import total_by_category, total_by_month, total_expenses
from src.loader import load_expenses
from src.filters import filter_by_category, filter_by_month

os.chdir('D:/Python/expenses_cli')


def main():
    expenses = load_expenses(
        Path("data/expenses_clean.csv")
    )

    total = total_expenses(expenses)

    category_totals = total_by_category(expenses)

    monthly_totals = total_by_month(expenses)

    print(f"Loaded {len(expenses)} expenses")
    print(f"Total expenses: {total:,.2f}")

    for category, total in sorted(
            category_totals.items(),
            key=lambda item: item[1],
            reverse=True):
        print(f"{category}: {total:,.2f}")

    for month, total in sorted(monthly_totals.items()):
        print(f"{month}: {total:,.2f}")

    category_expenses = filter_by_category(
        expenses, "entertainment"
    )

    total_category_expense = total_expenses(category_expenses)

    print(f"Selected Category Expense: {total_category_expense}")

    month_expenses = filter_by_month(
        expenses,
        2026,
        6
    )
    month_category = filter_by_category(
        month_expenses,
        "health"
    )

    total_category_expense_month = total_expenses(month_category)

    print(f"Health Expense in June: {total_category_expense_month}")

if __name__ == "__main__":
    main()

