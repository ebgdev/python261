# lst = [1,2,3,4,5]


# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst[4])


# print(lst[-1])
# print(lst[-2])
# print(lst[-3])
# print(lst[-4])
# print(lst[-5])

# -------------------------

# son iki elemani toplayarak yeni elemani elde edebiliriz.
# lst = [0,1,1,2,3,5,8,13]

# yeni_eleman = lst[-2] + lst[-1]
# lst.append(yeni_eleman)
# print(lst)


# -------------------------

# lst= [0,1]

# for _ in range(10):
#     lst.append(lst[-2]+lst[-1])

# print(lst)


# -------------------------# -------------------------# -------------------------

# what are tuples ?
    # orderd (ben hangi sirada yazdiysam o sirada tutulur, sirayi kendi kafasina gore bozmaz)
    # unchangeble/immutable 
    # eger bir veri uzun sure boyunca degistirilmeyecekse o zaman tuple kullaniriz

# my_tuple = ('berke','yusuf','aynaz','damla')
# # my_tuple.append('erfan') # AttributeError
# # my_tuple[0] = 'erfan' # assignment (TR: atama) desteklenmiyor
# # print(my_tuple[0])


# # iterable
# for item in my_tuple:
#     print(item)


# ---------------------
# # tek elemanli bir tuple:


# # int ✅
# # tuple ❌
# my_tpl = (30)
# print(type(my_tpl))

# # int ❌
# # tuple ✅
# a_tpl = (30,)
# print(type(a_tpl))


# a_tpl.append(40)


# ---------------------
# note : ic ice listeler

# my_list = [1,2,[4,5,6]]
# yeni_liste = my_list[2] # [4,5,6]

# print(yeni_liste[1]) # 5

# print(my_list[2][1]) # 5



# ----------------------------------

# # aranan eleman 11: 
# # nasil 11'i yazdirabiliriz.
# my_list = [1,   2,   3,  4,   [  5,   6,   [   7, 8 ,9 , [10,11]   ]  ]     ]

# # print(my_list[4][2][3][1])
# print(my_list[-1][-1][-1][-1])


# Note Sonu
# ----------------------------------soru----------------------------------

# my_tuple = (10,'yusuf',(1,2,3),[4,5,6],3.14,[])

# # my_tuple[0] = 100 # TypeError
# # my_tuple[1] = 'erfan' # TypeError
# # my_tuple[2] = (1.1,2.2,3.3) # TypeError
# # my_tuple[3] = [7,8,9] # TypeError
# my_tuple[3][0] = 40 # my_tuple[3] kisim artik bir liste, ve listede elemanlar degistirilebilir.
# lst = my_tuple[3]
# lst[1] = 50

# # ---------
# # # # 1.yontem
# # # my_tuple[5] = ['erfan'] #TypeError
# # foo = my_tuple[5]
# # # foo.append('erfan','yusuf') # Hata: append tek bir arguman ekler
# # # foo.append(['erfan','yusuf']) # ic ice liste verir
# # foo.extend(['berke','yusuf','damla','aynaz'])
# # ---------
# # # 2.yontem
# foo = my_tuple[5] # tuple'daki bos listem: []
# ogrenciler = ['aynaz','yusuf','damla','berke']

# for ogrenci in ogrenciler:
#     foo.append(ogrenci)

# # ---------


# print(my_tuple) # (10,'yusuf',(1,2,3),[4,5,6],3.14,['berke','yusuf','damla','aynaz'])
# print(my_tuple[5][3])


# ----------------------------------soru-sonu---------------------------------


# # liste ve tuple ozellikleri ve sayilari:

# a_tuple = (1,2,3,4)
# a_list = [1,2,3,4]


# print(len(dir(a_list))) # listeler icin 48 adet ozellik var
# print(len(dir(a_tuple))) # tuple'lar icin 35 adet ozellik var