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
    return sorted_operations


def print_last_operations(operations: list) -> list:
    """
    Return last five operations
    :param operations:
    :return:
    """
    latest_operations = operations[:5]
    return latest_operations


def get_instances(transactions: list) -> list:
    """
    Get instances from transactions
    :param transactions:
    :return:
    """
    operation_instances = []
    for operation in transactions:
        if operation:
            operation_instance = Transaction(
                date=operation["date"],
                description=operation["description"],
                trans_from=operation.get("from", ""),
                trans_to=operation["to"],
                amount=operation["operationAmount"]["amount"],
                currency=operation["operationAmount"]["currency"]["name"],
            )
            operation_instances.append(operation_instance)
    return operation_instances
