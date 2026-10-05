import os
from pathlib import Path

from src.analytics import total_by_category, total_by_month, total_expenses
from src.filters import filter_by_category, filter_by_month
from src.loader import load_expenses
from src.validation import detect_encoding, is_utf8_encoding, validate_file_exists, validate_file_type
from src.encoding import convert_to_utf8

os.chdir('D:/Python/expenses_cli')


def main():
    file_path = Path("data/raw/expenses_latin1.csv")
    validate_file_exists(file_path)
    validate_file_type(file_path)
    print("Valid File Type")

    encoding, confidence = detect_encoding(file_path)
    print(f"Detected encoding: {encoding}")
    print(f"Confidence: {confidence:.2%}")

    if is_utf8_encoding(encoding):
        print("File is already UTF-8.")
        output_path = file_path
    else:
        output_path = Path(
            "data/processed/input_utf8.csv"
        )

        convert_to_utf8(
            file_path,
            encoding,
            output_path,
        )

        print(f"Converted file to UTF-8: {output_path}")

    expenses = load_expenses(
        output_path
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

