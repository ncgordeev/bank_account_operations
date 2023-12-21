import pytest
from src.main_class import Transaction
from config import TEST_FILE_PATH
from src.utils import load_transactions_from_file, sorted_transactions


def test_load_transactions_from_file():
    operations = load_transactions_from_file(TEST_FILE_PATH)
    assert operations == [{"1": 1, "2": 2, "3": 3}]
