# ogrenciler = ["damla","berat"]


# ogrenciler.append("aynaz")
# # ogrenciler.append(["aynaz","ahmet"])
# ogrenciler.extend(["berke","yusuf"])
# # ogrenciler.clear()
# # ogrenciler = []
# print("ogrenciler:",ogrenciler)

# # ogrenciler2 = ogrenciler # ❌
# ogrenciler2 = ogrenciler.copy() # ogrenciler2 = ["damla","berat","aynaz","berke","yusuf"]
# print("ogrenciler2:",ogrenciler2)

# ogrenciler.append("erfan")

# print("ogrenciler:",ogrenciler)
# print("ogrenciler2:",ogrenciler2)


# ----------------------------------

# my_arr = ["erfan","berke","berat","damla","berke","yusuf","berke"]

# to_search = "berke"
# count = 0
# for name in my_arr:
#     if name == to_search:
#         count += 1
# print(count)

# --------------
# locations = []

# for index in range(len(my_arr)):
#     if my_arr[index] == to_search:
#         locations.append(index)

# print(locations)

# my_arr.insert(3,"muhammet")
# print(my_arr.count("berke"))
# print(my_arr.index("berke",5))
# silinen_eleman = my_arr.pop() # sildigi elemani kaydebilir
# print(silinen_eleman)


# # my_arr.remove("umut") # eleman varsa siler, yoksa hata uretir, eleman sayisi fazlaysa ilk elemani siler.
# print(my_arr)


# ----------------------------------------------------

# my_arr = ["erfan","berke","berat","damla","berke","yusuf","berke"]

# yontem1:
# to_search = "berke"
# while to_search in my_arr:
#     my_arr.remove(to_search)

# print(my_arr)


# --------------------------
# yontem2:
# to_search = "berke"
# for name in my_arr:
#     if name == to_search:
#         my_arr.remove(to_search)

# print(my_arr)



# ----------------------------------------------------

# my_arr = ["erfan","berke","berat","damla","berke","yusuf","berke"]

# my_arr.reverse() # kalici olarak listemi tersliyor
# my_arr.sort() # kalici olarak listeyi siraliyor
# print(my_arr)


# ----------------------------------------------------


# my_arr = ["erfan","berke","berat","damla","berke","yusuf","berke","aynaz","berat","yusf"]
# my_arr2= [11,22,33,11,22,11,44,55,11,22,66,33]

# def kac_tane(liste,aranan):
#     sayac = 0
#     for name in liste:
#         if name == aranan:
#             sayac += 1
#     print(sayac)


# kac_tane(my_arr,"berat")
# kac_tane(my_arr2,33)


# ----------------------------------------------------

# a = 1000 # bu sayilar fonksiyonun parameterlerini etkilemez
# b = 2000

# def add(a,b):
#     return (a+b) # donus degeri


# def tek_mi(sayi):
#     if sayi % 2 == 0:
#         return f"hayir {sayi} cift"
#     else:
#         return f"evet {sayi} tek"

# print(add(100,30))
# print(add(120,180))

# print(tek_mi(11))
# print(tek_mi(12))


# bir fonksiyon yaziniz 
# bu fonksiyon 2 sayi alsin
# bu iki sayinin carpimi ne olur dondursun

# ------------

# def carpma(a,b):
#     return a*b

# print(carpma(12,5)) # 60
# print(carpma(0,1000))




# ----------------------------------------------------

# bir fonksiyon yaziniz 
# bu fonksiyon bir liste ve bir sayi parametre olarak alacak
# sonra o listede o sayi var mi diye kontrol edecek 
# varsa True
# yoksa False donecek.

a_list = [11,22,33,44,55,66,12]
a_num = 11
b_num = 12
c_num = 33
d_num = 45

# yontem1:

# def is_in_list(liste,sayi):
#     if sayi in liste:
#         return True
#     else:
#         return False    


# yontem2:
def is_in_list(liste,sayi):
    for number in liste:
        if number == sayi:
            return True
    return False


# -------------------

print(is_in_list(a_list,a_num)) # True
print(is_in_list(a_list,b_num)) # False
print(is_in_list(a_list,c_num)) # True
print(is_in_list(a_list,d_num)) # False