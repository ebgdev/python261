# -----------------# yontem1:---------------
# my_arr = ['ahmet','mehmet','ahmet','yusuf','onur','ahmet','onur']

# konumlar = []

# for index in range(len(my_arr)): # range(7) --> 0,1,2,3,4,5,6
#     if my_arr[index] == 'ahmet':
#         konumlar.append(index)

# print(konumlar)

# ----------------# yontem2:----------------
# my_arr = ['ahmet','mehmet','ahmet','yusuf','onur','ahmet','onur']


# konumlar = ''

# for index in range(len(my_arr)): # range(7) --> 0,1,2,3,4,5,6
#     if my_arr[index] == 'ahmet':
#         konumlar+= f'-{index}'
# print(konumlar)

# --------------------------------
# enumerate() dongusu
# kelime anlami : numaralandir demektir.
# range'den cok daha hizli calisir.

# my_arr = ['ahmet','mehmet','ahmet','yusuf','onur','ahmet','onur']

# # for x in enumerate(my_arr):
# #     # print(x) # hem konumunu , hem elemanin kendisini verir
# #     # print(x[0])
# #     # print(x[1])
# #     print(x[0],x[1])


# # for index , name in enumerate(my_arr):
# #     # print(index)
# #     # print(name)
# #     # print(index,name)
# #     print(f"index:{index} ve elemanimiz: {name}")

# # ilk gelen index
# # ikinci gelen eleman olur.
# for a,b in enumerate(my_arr):
#     print(a,b)

# print('---------------')

# for index in range(len(my_arr)):
#     print(index,my_arr[index])

# --------------------------------
# while dongusu --> bir sey oldugu surece devam et
# numbers = [11,22,33,44,55]
# index = 0
# length = len(numbers)

# while index < length: # 0 < 5
#     print(numbers[index])
#     index+=1


# -------------------------------------------

# scores = [100,49,50,51,70,90,30,21]
# students = ['ahmet','tunahan','yusuf','fatih','sevval','nazli','bahadir','erfan']
# # ------------------------
# # yontem1: enumerate ile.
# # ------------------------
# result = []

# for index,score in enumerate(scores):
#     if score >= 50:
#         result.append(students[index])
# print(result)


# ------------------------
# yontem2: while ile.
# ------------------------
# result = []

# index = 0
# while index < len(scores): # 0 < 8
#     if scores[index] >= 50:
#         result.append(students[index])
#     index += 1

# print(result)



# -------------------------------------------

scores = [100,49,50,51,70,90,30,21]
# Toplayiniz
# ---------
# # 1.Normal For ile
# result = 0
# for score in scores:
#     result += score
# print(result)

# ---------
# 2.for range ile
# result = 0
# for index in range(len(scores)): # range(8) -> 0,1,2,3,4,5,6,7
#     result += scores[index]
# print(result)
# ---------
# 3. for enumerate ile
result = 0
for index,score in enumerate(scores):
    result += score

print(result)

# # ---------
# # 4. while ile
# result = 0
# index = 0
# while index < len(scores):
#     result += scores[index]
#     index += 1

# print(result)