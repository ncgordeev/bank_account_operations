from pathlib import Path

ROOT_PATH = Path(__file__).parent
OPERATIONS_PATH = Path.joinpath(ROOT_PATH, "files", "operations.json")
TEST_FILE_PATH = Path.joinpath(ROOT_PATH, "tests", "test_trans.json")