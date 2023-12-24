from config import OPERATIONS_PATH
from src.utils import load_transactions_from_file, sorted_transactions, get_class_instances


def main():
    operations = load_transactions_from_file(OPERATIONS_PATH)
    sorted_data = sorted_transactions(operations)
    transactions = get_class_instances(sorted_data)
    for transaction in transactions:
        print(transaction)


if __name__ == "__main__":
    main()
