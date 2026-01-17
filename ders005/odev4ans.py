puanlar = [20, 90, 77, 60, 91, 0, 100, 99]
temp_min = puanlar[0] # 20
temp_max = puanlar[0] # 20 - 90

for index in range(1,len(puanlar)): # range(8) -> 0 ❌, 1,2,3,4,5,6,7
    if puanlar[index] > temp_max:
        temp_max = puanlar[index]
    if puanlar[index] < temp_min:
        temp_min = puanlar[index]

print(f"Max: {temp_max}, Min:{temp_min}")


# beklenen cikti: Max: 100, Min:0

# -------------------------------------------------

# eleman , listeniz[index]
# sadece tek indisli isimleri yazdiriniz.
# ciktiyla bire bir ayni sonuca ulasmaya calisniz.

isimler = ['damla','berke','aynaz','berat','erfan','emre']

# Beklenen cikti:
# 1.berke
# 3.berat
# 5.emre

# print(isimler[0])
# print(isimler[1])
# print(isimler[2])
# print(isimler[3])
# print(isimler[4])
# print(isimler[5])

# print("---------------")

# for index in range(len(isimler)): # range(6) -> 0,1,2,3,4,5
#     print(isimler[index])

# yontem1: bolduk ikiye eger kalan 1 ise
# for index in range(len(isimler)):
#     if index % 2 == 1:
#         print(f"{index}.{isimler[index]}")

# yontem2: bolduk ikiye eger kalan 0 degil ise
for index in range(len(isimler)):
    if index % 2 != 0:
        print(f"{index}.{isimler[index]}")




# -------------------------------------------------

# isimler listesindeki en uzun isim kime ait ve hangi indexte ?

isimler = ['damla','berke','aynaz','berat','erfan','emre','muhammet']


# Beklenen Cikti: 
# En uzun isim:muhammet 8 karakterden olusuyor ve 6 index'ine ait

# Yontem1:
temp_max = len(isimler[0])
temp_index = 0
for i in range(len(isimler)):
    if len(isimler[i]) > temp_max:
        temp_max = len(isimler[i])
        temp_index = i


print(f"En uzun isim:{isimler[temp_index]} {temp_max} karakterden olusuyor ve {temp_index}. index'ine ait")


# Yontem2:

max_len = 0
temp_isim = ''
for index in range(len(isimler)): # range(7) -> 0,1,2,3,4,5,6
    if len(isimler[index]) > max_len:
        max_len = len(isimler[index])
        temp_isim = isimler[index]


print(max_len,temp_isim)
