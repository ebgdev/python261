from pathlib import Path
from time import sleep

# # desired_output: 
# # name: Alice , age: 20
# # name: Bob , age: 22
# # name: Charlie , age: 19


# BASE_DIR = Path(__file__).resolve().parent
# file_path = (BASE_DIR / 'students.txt')

# with open(file_path) as f:
#     for line in f:
#         # result = line.strip().split(', ')
#         # name = result[0]
#         # age = result[1]
#         name,age = line.strip().split(', ')
#         print(f"name: {name} , age: {age}")


# ---------------------------------------------

# ✅ yield sadece fonksiyon icinde calisir

BASE_DIR = Path(__file__).resolve().parent
full_path = BASE_DIR / 'long_list.txt'

# def fetch_lines(file_name):
#     with open(file_name) as f:
#         lines = []
#         for line in f:
#             lines.append(line)
#         return lines
    
# print(fetch_lines(full_path))


def fetch_lines_yield(file_name):
    with open(file_name) as f:
        for line in f:
            yield line

call_line = fetch_lines_yield(full_path)
for i in range(3840000):
    print(next(call_line))


# ------------------------------------------

# file = open("filename.txt", "mode")

# "r"	Read (default). File must exist.
# "w"	Write. Creates or overwrites a file.
# "a"	Append. Adds to the end of a file.
# "x"	Create. Creates a new file, fails if it exists.
# "b"	Binary mode (e.g., images, videos).
# "t"	Text mode (default).

# /Users/ma/Desktop/files in python/new_dir # absolute path
# if path starts with (./) means go from current folder/directory
# if path starts with (../) means go from previous folder/directory
# all these forward slashes should become backward slash for windows OS
# in order to get rid of all these changes we can use built-in hashlib tool
# https://docs.python.org/3/library/pathlib.html
# from pathlib import Path

# with open("new_dir/example.py") as f:  # relative path
#     for line in f:
#         print(line)

# cd : Change Directory
# pwd: Print Working Directory (print current directory)
# ls : list
# ls -a: list all
# ls -l: list as list
# ls -la: list as list all
# cd ~: go to root
# mkdir: make directory (klasor olusturur)
# rm -rf <directory_name>: remove directory
# toch <file_name>: create a file, ex: touch name.txt
# echo hi berke > berke_sil_sonra.txt
# echo hi berke 1>> berke_sil_sonra.txt
# echo hi berke 1 >> berke_sil_sonra.txt
# cat: shows the file's content