from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'log.txt'
print(file_path)


with open(file_path) as f:
    print(f.read())


# Beklenen Cikti: ('error':3,'warning':2,...)


