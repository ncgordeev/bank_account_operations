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

    @staticmethod
    def formatting_date(date) -> str:
        formatted_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return formatted_date.strftime("%d.%m.%Y")

    def __str__(self) -> str:
        return f"{self.date}, {self.description},\n" \
               f"{self.trans_from}, {self.trans_to}, {self.amount}, {self.currency})"

    def __repr__(self) -> str:
        return f"Transaction({self.date}, {self.description},\n" \
               f"{self.trans_from}, {self.trans_to}, {self.amount}, {self.currency})\n"
