# set : kumeler
# A set is a collection which is unordered, unchangeable*, and unindexed.
# empty_set = set()


# aset = {'erfan','berke','yusuf','berke','meltem','erfan'}
# print(type(aset))
# print(aset)



# ---------------------------------------

# my_list = ['erfan','berke','yusuf','berke','meltem','erfan']
# # find unique items in list
# def find_uniqe(lst):
#     result = []
#     for item in lst:
#         if item not in result:
#             result.append(item)
#     return result


# print(find_uniqe(my_list)) # ['erfan', 'berke', 'yusuf', 'meltem']


# ---------------------------------------


# aset = {'erfan','berke','yusuf','berke','meltem','erfan','aynaz'}
# bset = {'erfan','berke','taha','soner'}


# print(aset | bset) # union
# print(aset.union(bset)) # union

# print(aset - bset) # fark
# print(aset.difference(bset)) # fark


# print(aset & bset) # ortak
# print(aset.intersection(bset)) # ortak



# --------------------------------------- dictionary -----------------------------------------
# kelime : anlami
# anhtar: deger
# key: value
# good : iyi
# well: iyi
# kind : iyi
# nice: iyi

# ---------

# Python Dictionary (Sözlük)

# Python 3.7'den önce:
# - Dictionary elemanları sıralı değildir (unordered).
# - Iterable'dır (üzerinde döngü kurulabilir).

# Python 3.7 ve sonrası:
# - Dictionary elemanları eklenme sırasını korur (ordered).
# - Iterable'dır.

# Önemli Kurallar:
# ✅ Anahtarlar (keys) benzersizdir (unique) → aynı anahtar iki kez olamaz.
# ✅ Değerler (values) tekrar edebilir.

# "in" anahtar kelimesi sadece anahtarları (keys) kontrol eder, değerleri değil.
# --------------------
# adict = {
#     'good': 'iyi',
#     'well': 'iyi',
#     'book': 'kitap'
# }

# print(type(adict))
# print(adict)
# --------------------

# my_dict = {"turkey":99,"usa":1,"canada":1,"germany":45}
# print(my_dict['germany'])
# # print(my_dict[0]) # Hata: KeyError

# # for key in my_dict:
# #     print(key,my_dict[key])

# print("turkey" in my_dict)
# print(45 in my_dict)


# ---------------------
# lst = ['banana','orange','banana','apple','orange','kiwi','banana','watermelon','apple']
# # output: ('banana':3,'orange':2,'apple':2,'kiwi':1,'watermelon':1)

# result = {}

# for item in lst:
#     if item not in result:
#         result[item] = 1
#     else:
#         result[item] += 1

# print(result)

# -------------------------------------------------------

adict = {'banana': 3, 'orange': 2, 'apple': 2, 'kiwi': 1, 'watermelon': 1}


# # print(adict['grape']) # Hata verir: KeyError
# print(adict.get('banana','not found'))
# print(adict.get('grape','bulunamadi'))
# print(adict.get('grape','null'))
# print(adict.get('grape',0))
# print(adict.get('grape',1))

# adict['banana'] = 6
# adict.update({'cherry':1})
# adict.update({'banana':10})

# print(adict.keys())
# print(list(adict.keys()))

# print(list(adict.values()))

# print(list(adict.items()))

# print(adict)


# ---------------------------------------------

# adict butun elemanlarini key,value ciftli sekilde yazmak istiyoruz

for key in adict:
    print(key,adict[key])

print('------------------')
# daha hizli, verimli

for key,value in adict.items():
    print(key,value)