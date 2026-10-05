from datetime import date

from .models import Expense


def filter_by_category(
        expenses: list[Expense],
        category: str,
) -> list[Expense]:
    return [
        expense for expense in expenses if expense.category.lower() == category.lower()
    ]

def filter_by_month(
        expenses: list[Expense],
        year: int,
        month: int,
) -> list[Expense]:
    return [
        expense for expense in expenses 
        if expense.date.year == year 
        and 
        expense.date.month == month
    ]