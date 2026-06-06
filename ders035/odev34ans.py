from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / 'log.txt'
print(file_path)


with open(file_path) as f:
    logs = f.read().split(' ')
    result = Counter(logs) # result Counter objecttir
    print(result)
    print(dict(result))

# Beklenen Cikti: ('error':3,'warning':2,...)