from datetime import datetime


class Transaction:
    """
    This class describes the transactions from json-file
    """

    def __init__(self, date: str, description: str, trans_from: str,
                 trans_to: str, amount: float, currency: str) -> None:
        self.date = date
        self.description = description
        self.trans_from = trans_from
        self.trans_to = trans_to
        self.amount = amount
        self.currency = currency

    def __str__(self) -> str:
        return f"{self.date}, {self.description},\n" \
               f"{self.trans_from}, {self.trans_to}, {self.amount},\n" \
               f"{self.currency})"

    def __repr__(self) -> str:
        return f"Transaction({self.date}, {self.description},\n" \
               f"{self.trans_from}, {self.trans_to}, {self.amount},\n" \
               f"{self.currency})"
