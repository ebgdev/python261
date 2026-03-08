# ------------------ use customized function in filter ---------------------

# import math
# new_array = [i for i in range(1,101)]

# def is_prime(num) -> bool:
#     if num <= 1:
#         return False
#     for i in range(2,(num//2)+1):
#         if num % i == 0:
#             return False
#     return True

# prime_numbers = list(filter(is_prime,new_array))
# print(prime_numbers)

# --------------------------- Manual Map Function -----------------------------

# my_list = [i for i in range(1,11)]
# print(my_list)


# ten_added_list = list(map(lambda x: x+10,my_list))
# print(ten_added_list)


# def my_map(my_func,my_iter):
#     lst = []
#     for iter in my_iter:
#         lst.append(my_func(iter))
#     return lst


# print(my_map(lambda x: x**2,my_list)) # [1,4,9,16,25,36,49,64,81,100]

# --------------------------- Nested Lists & Loops --------------------------
# 2D Arrays
# iç içe listeler ve döngüler

my_list = [[1,2,3],['berke','yusuf','aynaz','erfan'],[19,20,21,22,23]]

# print(my_list[2][1]) # 20

# 1
# 2
# 3
# berke
# yusuf
# ...
# 20
# 21
# ------------

# Normal For Loop:

# for big_item in my_list:
#     for small_item in big_item:
#         print(small_item)

# ------------

# For Range Loop:
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[i][j])


# ------------

# While Loop:

# i = 0
# while i < len(my_list):
#     j = 0
#     while j < len(my_list[i]):
#         print(my_list[i][j])
#         j+=1
#     i+=1


# ------------

# enumerate1:



# ------------
# enumerate2: