from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
full_path = BASE_DIR / 'names.txt'


# readlines:


with open(full_path) as f:
    print(f.readlines()) # return value type is a list