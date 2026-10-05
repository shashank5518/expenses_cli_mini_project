from collections import defaultdict
from decimal import Decimal

from src.models import Expense


def total_expenses(expenses: list[Expense]) -> Decimal:
    return sum(
        (expense.amount for expense in expenses),
        Decimal("0"),
    )

def total_by_category(expenses: list[Expense],) -> dict[str, Decimal]:
    totals: dict = defaultdict(lambda: Decimal("0"))

    for expense in expenses:
        totals[expense.category] += expense.amount

    return dict(totals)

def total_by_month(expenses: list[Expense]) -> dict[str, Decimal]:
    totals: dict = defaultdict(lambda: Decimal("0"))

    for expense in expenses:
        month = expense.date.strftime("%Y-%m")
        totals[month] += expense.amount
    return dict(totals)