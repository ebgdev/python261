from pathlib import Path

lst = ['berke', 'yusuf', 'faruk', 'emirhan']

file_path = Path(__file__).parent / "names.csv"

with open(file_path, mode="w", encoding="utf-8") as f:
    f.write("id,name\n")
    for i, name in enumerate(lst, start=1):
        f.write(f"{i},{name}\n")