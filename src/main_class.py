from datetime import datetime


class Transaction:
    """
    This class describes the transactions from json-file
    """

    def __init__(self, date: str, description: str, trans_from: str,
                 trans_to: str, amount: float, currency: str) -> None:
        self.date = self.formatting_date(date)
        self.description = description
        self.trans_from = self.masking_number(trans_from)
        self.trans_to = self.masking_number(trans_to)
        self.amount = amount
        self.currency = currency

    @staticmethod
    def formatting_date(date: str) -> str:
        formatted_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return formatted_date.strftime("%d.%m.%Y")

    @staticmethod
    def masking_number(card_or_account_number: str) -> str:
        if card_or_account_number is None:
            return f"Открыт новый счет"
        split_number = card_or_account_number.split()

        if card_or_account_number.startswith("Счет"):
            number_for_masking = split_number.pop()
            masking_number = f"**{number_for_masking[-4:]}"
            split_number.append(masking_number)
        else:
            number_for_masking = split_number.pop()
            masking_number = f"{number_for_masking[:6] + ' ** **** ' + number_for_masking[-4:]}"
            split_number.append(masking_number)
        return " ".join(split_number)

    def __str__(self) -> str:
        return f"{self.date} {self.description}\n" \
               f"{self.trans_from} -> {self.trans_to}\n" \
               f"{self.amount} {self.currency}\n"

    def __repr__(self) -> str:
        return f"(Transaction({self.date} {self.description} \
                 {self.trans_from} {self.trans_to} \
                 {self.amount} {self.currency}))"
