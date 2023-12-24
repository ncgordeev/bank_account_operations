import json
from src.main_class import Transaction


def load_transactions_from_file(file_path: str) -> list:
    """
    Load transactions from json-file
    :param file_path:
    :return:
    """
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)
        return data


def sorted_transactions(transactions: list) -> list:
    """
    Sort transactions by date
    :param transactions:
    :return:
    """
    operations = [operation for operation in transactions if operation.get("state") == "EXECUTED"]
    sorted_operations = sorted(operations, key=lambda x: x["date"], reverse=True)
    latest_operations = sorted_operations[:5]
    return latest_operations


def get_class_instances(sorted_operations: list) -> list:
    transactions = []
    for transaction in sorted_operations:
        transaction_obj = Transaction(
            transaction.get("date"),
            transaction.get("description"),
            transaction.get("from"),
            transaction.get("to"),
            transaction["operationAmount"]["amount"],
            transaction["operationAmount"]["currency"]["name"],
        )
        transactions.append(transaction_obj)
    return transactions
