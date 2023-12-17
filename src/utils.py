import json


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
    return sorted_operations
