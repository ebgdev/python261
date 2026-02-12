# odemeler = ['200','30.5','120','30.2','100']


# def find_min_number(lst):
#     temp_min=float(lst[0]) # range, while , genel anlamda eger index ile listeyi dolasiyorsak
#     # elamana lst[index] 'leri seklinde erisiriz.
#     for i in range(1,len(lst)):
#         if float(lst[i])<temp_min:
#             temp_min=float(lst[i])
#     return temp_min

# print(find_min_number(odemeler))

# -------------------list-unpacking-------------------

# info = ["erfan",28,False]
# name, age, is_married = info

# print(name)
# print(age)
# print(is_married)

# -----------------------------------------------------

# mercedes , *vw, bmw = ['smart','lamborgini','bently','skoda','audi','bugatti','mini']

# print(f"mercedes: {mercedes}")
# print(f"vw: {vw}")
# print(f"bmw: {bmw}")


# ------------------- list-slicing -------------------

# numbers = [11,22,33,44,55,66,77,88,99,110]
# # sytax (TR:soz dizilimi) numbers[start:end:step]
# # end kismi exclusive, yani kendisi dahil degildir.

# lst1 = numbers[0:4:2] 
# lst2 = numbers[1::3] # 1,4,7
# lst3 = numbers[::1] # baslangic: 0, son: son, adim: 1
# lst4 = numbers[::-1] # baslangic: 0, son: son, adim: 1
# print(numbers[0:3]) # [11,22,33] , # baslangic: 0 --> 11, son:index 2 --> 33 , adim: 1
# # print(lst4)

# --------------------
# # 1.yontem: listeyi ters cevirmek icin
# new_list = []
# new_list = numbers.copy()
# new_list.reverse()

# print(f"numbers: {numbers}")
# print(f"new list: {new_list}")

# --------------------

# # 2.yontem: listeyi ters cevirmek icin
# ters_liste = numbers[::-1]

# print(f"Numbers: {numbers}")
# print(f"Ters list: {ters_liste}")


# ---------------------------------------------

# str1 = "name"
# str2 = "ada"
# str3 = "ata"

# print(str3[::-1])

lst = ['berke',
        'ada',
        'kazak',
        'tarak',
        'faruk',
        'ses',
        'yusuf',
        'radar'
    ]

# eger bir kelime , tersine esit ise , o kelime polindormdur.
# def is_palindorme(word): # boolen value: True/False
#     if word == word[::-1]:
#         return True
#     else:
#         return False


# print(is_palindorme(lst[0])) # False
# print(is_palindorme(lst[1])) # True

# ---------------------
# beklenen cikti:

# berke is not polindorme
# ada is plolindorme
# kazak is polindorme
# tarak is not polindorme


def is_palindorme(word):
    return word == word[::-1]


def check_lst(lst):
    for word in lst:
        if is_palindorme(word):
            print(f"{word} is palindorme.")
        else:
            print(f"{word} is not palindorme.")


# print(check_lst(lst)) # --> None verir cunku bu fonksiyon bir sey donmuyor (return degeri yok).
check_lst(lst)