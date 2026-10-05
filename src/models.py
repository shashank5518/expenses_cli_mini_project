from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Expense:
    date: date
    description: str
    category: str
    amount: Decimal
    payment_method: str