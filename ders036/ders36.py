# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent
# full_path = BASE_DIR / 'names.txt'


# lst = ['berke','yusuf','faruk','emirhan']

# # ‼️ dikkat w dosyanin uzerine yazar. dosyaya eklemek icin 'a' kullanmaliyiz
# with open(full_path,mode="w") as f: 
#     for name in lst:
#         if name == lst[-1]:
#             f.write(f"{name}")
#         else:
#             f.write(f"{name}\n")

# ---------------------------------------------------
# ✅ Turkce karakter icin : utf8 kullaniriz
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent
# full_path = BASE_DIR / 'names.txt'


# lst = ["birinci", "ikinci", "üçüncü"]

# with open(full_path,mode="w",encoding='utf8') as f: 
#     for name in lst:
#         f.write(f"{name}")
        

# ---------------------------------------------------

# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent
# full_path = BASE_DIR / 'names.txt'


# lst = ["dördüncü", "beşinci", "altıncı"]

# with open(full_path,mode="a",encoding='utf8') as f: 
#     for name in lst:
#         f.write(f"\n{name}")


#     # f.write('\n----------------------------\n\n')
#     # f.write('\nresult: 10 failed, 20 successfull')


# ---------------------------------------------------

# # bir iterable (list,tuple,dict,set, ...) uzerindeki degerleri
# # dongu kurmadan yazmaya yarar
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent
# full_path = BASE_DIR / 'names.txt'


# lst = ["dördüncü\n", "beşinci\n", "altıncı\n"]

# with open(full_path,mode="a",encoding='utf8') as f: 
#     f.writelines(lst)


# ---------------------------------------------------

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
full_path = BASE_DIR / 'id_names.txt'
lst = ['berke','yusuf','faruk','emirhan']

# beklenen cikti: id_names.txt dosyasinda
# id,name
# 1,berke
# 2,yusuf
# 3,faruk
# 4,emirhan


