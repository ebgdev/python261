# ogrenciler = ['berat','berke','damla','aynaz','erfan']

# # for stu in ogrenciler:
# #     print(stu)

# # -----------------------------

# # range fonksiyonun, her zaman bir tam sayi alir.
# # len(ogrenciler) = 4
# # range(4) --> range[0,4) --> 0,1,2,3


# for index in range(len(ogrenciler)):
#     print(index,ogrenciler[index])


# -----------------------------# -----------------------------

# user_name = 'erfan bahcivan'

# # 0.   e
# # 1.   r
# # 2.   f
# # 3.   a

# for index in range(len(user_name)):
#     print(index,user_name[index])

# -----------------------------# -----------------------------

# name = 'berat'

# for index in range(len(name)): # range(5) -> 0,1,2,3,4
#     print(f"indisimiz: {index} , eleman: {name[index]}")

# -----------------------------# -----------------------------

# # yukaridaki kodu yapip bitiren asagidaki kodu cozebilir

# cites = ['ankara','istanbul','eskisehir','tokat','izmir','samsun']
# # kodunuzu burada yaziniz

# # beklenen cikti:
# # cikti bire bire asagidaki gibi olmalidir

# # 0.ankara
# # 1.istanbul
# # 2.eskisehir
# # ....
# # 5.samsun

# for index in range(len(cites)):
#     print(f"{index}.{cites[index]}")

# -----------------------------# -----------------------------

cites = ['istanbul','eskisehir','tokat','izmir','samsun','ankara']

cites.append('trabzon')
cites.sort() # kalici olarak bu listeyi siraladi
print(cites)

for city in cites:
    print(city)