import json


def load_transactions_from_file(file_path):
    """
    Load transactions from json-file
    :param file_path:
    :return:
    """
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)
        return data
