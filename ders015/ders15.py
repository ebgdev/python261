# -------------------------------------------------- map() --------------------------------------------------

# import math
# # number = 5
# # print(math.pow(number,2))

# sayilar = [1, 2, 3, 4, 5, 6]

# # ---------------------------------------------

# sayilarin_karesi = ((lambda x: x**2)(x)for x in sayilar)

# for sayi in sayilarin_karesi:
#     print(sayi)

# # ---------------------------------------------
# print("------------------------")
# # ---------------------------------------------

# # map

# # elimdeki butun elemanlari, islemime gore haritalandir.
# # eger islem x**2 ise 
# # ve listem: sayilar = [1, 2, 3, 4, 5, 6]
# # mapping : listemdeki butun elemanlari bu isleme gore haritalandiriyor.
# # dolayisiyla map fonksiyonu kendisi otomatik bir sekilde bir donguyu taklit ediyor

# # map(func, iterable):
# sayilarin_karesi1 = map(lambda x: x**2,sayilar) # (1,4,...,36)
# for sayi in sayilarin_karesi1:
#     print(sayi)


# --------------------------------------------------# --------------------------------------------------
# # map ile:
# sayilar = [1, 2, 3, 4, 5, 6]
# # Tek/Çift Kontrolü: Bir sayının çift olup olmadığını True veya False 
# # olarak döndüren bir lambda fonksiyonu yazın ve bunu bir değişkene atayarak sayılar listesi için test edin.
# # Tek ise False
# # Cift ise True

# tek_cift = list(map(lambda x: x%2==0,sayilar))
# print(tek_cift)
# print(1%2==0)


# --------------------------------------------------# --------------------------------------------------
# # ipucu:

# name = "erfan"
# print(name.capitalize())

# # map ile cozunuz
# # İsim Temizleme: Aşağıdaki listeyi, lambda kullanarak tüm isimlerin 
# # baş harfi büyük olacak şekilde güncelleyin:
# isimler = ("ahmet", "ayşe", "mehmet", "zeynep")

# capitalized_names = list(map(lambda item: item.capitalize(),isimler))
# print(capitalized_names)

# -------------------------------------------------- filter() --------------------------------------------------
# # filter(function, iterable)
# ages = [11,17,55,18,20,2,23]

# gte_18 = list(filter(lambda x:x>=18,ages))
# print(gte_18)


# ----------------------
# # map-filter
# # numbers listesindeki butun elemanlar 10 ile carpilicak
# # sonra bu liste icinden 50 >= olan elemanlar secilicek

# numbers = [3, 5, 7, 10, 15, 20, 25]

# mult_10  = list(map(lambda x: x*10,numbers))

# age_gte_50 = list(filter(lambda x: x >= 50,mult_10))
# print(age_gte_50)


# ----------------------

names = ["emir","esra","yusuf","Zehra","berke","erfan","zerrin","aynaz","onur","Elsa","ZEYNEP"]


# Select the names start with letter (z or Z)
names_start_with_z = list(filter(lambda x: x[0].lower() == "z",names ))
print(names_start_with_z)


# Select the names start with letter (E,e,z,Z)
names_start_with_e_z = list(filter(lambda x: x[0] in ['e','E','z',"Z"],names ))
print(names_start_with_e_z)