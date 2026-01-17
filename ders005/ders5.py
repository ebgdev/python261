# kisiler = []


# kisiler.append('berat') # adds to the end of the list.
# kisiler.append('damla')
# kisiler.append(3.14)
# kisiler.append('berke')
# kisiler.append('aynaz')
# kisiler.append(100)
# kisiler.append('ahmet')
# kisiler.append(True)

# print(type(kisiler))
# print(type(kisiler[0]))
# print(type(kisiler[2])) # class float
# print(kisiler)


# ------------------------------------
# # Bir for dongusu kurunuz oyle ki sadece str degerlerini yazdirsin.

# my_list = ['berat', 'damla', 3.14, 'berke', 'aynaz', 100, 'ahmet', True,200]


# # Yontem1:
# # for i in range():
# # range tam sayi alir. ne kadar gitmek istiyorsak o degeri girmemiz lazim (int cinsinden)
# # eger listemin uzunlugu kadar gideceksem len() kullanilirim 
# # sonuc olarak range(x) , liste gibi bir deger uretir (iteratif-dolasabilecegim)

# for index in range(len(my_list)): # 0,1,2,3,4,5,6,7,8✅ -9❌
#     if type(my_list[index]) == str:
#         # print(index,my_list[index])
#         print(f"index:{index}, element: {my_list[index]}")

# --------------# --------------# --------------
# Yontem2:
# standard for ile:

# for eleman in my_list:
#     if type(eleman) == str:
#         print(eleman)


# ------------------------------------------------

my_arr = ['apple','banana','apple','banana','apple','kiwi','orange','apple','orange']

# bu listede kac tane "apple" var ?
# for standard/range ile bulmaya calisiniz.

counter = 0
fruit_searching = "apple"

for fruit in my_arr:
    if fruit == fruit_searching:
        # counter = counter + 1 # c gibi dillerde isinize yarar
        counter += 1 # counter'un degeri neyse ona 1 ekle.

print(f"I found {counter} {fruit_searching}s in the list. ")