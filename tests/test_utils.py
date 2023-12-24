import json
import random

import pytest
from src.main_class import Transaction
from config import OPERATIONS_PATH, TEST_FILE_PATH, TEST_EMPTY_JSON
from src.utils import load_transactions_from_file, sorted_transactions, get_class_instances


def test_load_transactions_from_file():
    operations = load_transactions_from_file(TEST_FILE_PATH)
    assert operations == [{"1": 1, "2": 2, "3": 3}]


def test_load_empty_file():
    with pytest.raises(json.JSONDecodeError):
        load_transactions_from_file(TEST_EMPTY_JSON)


def test_load_file_not_exist():
    with pytest.raises(FileNotFoundError):
        load_transactions_from_file("test.json")


def test_get_class_instances():
    operations = load_transactions_from_file(OPERATIONS_PATH)
    sorted_operations = sorted_transactions(operations)
    operations = get_class_instances(sorted_operations)
    assert isinstance(operations[random.randint(0, 5)], Transaction)
