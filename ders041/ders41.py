# Algorithms - Algoritmalar

# Time Complexity : Zaman karmasikligi

# my_list = [1,2,3,4,5,6,7,8,9,112,563,1034]
# T(n) = 1'i bulmak  Ω(1)
# T(n) = 7'i bulmak  θ(7)
# T(n) = 1034'i bulmak  O(n)

# --------------------------------------

# bu ders kapsaminda 3 tane latin karakterini gorecegiz
# - Omega          :  Ω  :   Best Case
# - Theta          :  θ  :   Avrage Case
# - Omicron(big o) :  O  :   Worst Case

# --------------------------------------

# def print_numbers(x):
#     return 5

# print(print_numbers(10))
# print(print_numbers(100))

# # T(n) = O(1)


# --------------------------------------

# def print_numbers(n):
#     counter = 0
#     for i in range(n): # 0,1,2,3,4,5,6,7,8,9
#         counter += 1
#     return counter

# print(print_numbers(10)) # O(10)
# print(print_numbers(20)) # O(20)
# print(print_numbers(30)) # O(30)

# # print(print_numbers(n)) = O(?) --> O(n)

# --------------------------------------

# def print_numbers(n):
#     counter = 0
#     for i in range(n): # 0,1,2,3,4,5,6,7,8,9
#         counter += 1

#     for j in range(n): # 0,1,2,3,4,5,6,7,8,9
#         counter += 1

#     return counter

# print(print_numbers(10)) # O(20)
# print(print_numbers(20)) # O(40)
# print(print_numbers(30)) # O(60)

# # print(print_numbers(n)) = O(?) --> O(2n)


# --------------------------------------

# def print_numbers(n):
#     counter = 0
#     for i in range(n): # 0,1,2,3,4,5,6,7,8,9
#         counter += 1

#     for j in range(n): # 0,1,2,3,4,5,6,7,8,9
#         counter += 1

#     for t in range(n): # 0,1,2,3,4,5,6,7,8,9
#         counter += 1

#     return counter

# print(print_numbers(10)) # O(30)
# print(print_numbers(20)) # O(60)
# print(print_numbers(30)) # O(90)

# # print(print_numbers(n)) = O(?) --> O(3n)

# donguler alt altayken toplanir ✅
# --------------------------------------

# def print_numbers(n):
#     counter = 0
#     for i in range(n): # 0,1,2,3
#         for j in range(n): # 0,1,2,3
#             counter += 1
#             print(i,j)

#     return counter


# print(print_numbers(2)) # O(4)
# print(print_numbers(3)) # O(9)
# print(print_numbers(4)) # O(16)

# # print(print_numbers(n)) = O(n^2) --> O()
# # donguler ic iceyken islem sayilarini carpariz ✅
# --------------------------------------

# def print_numbers(n):
#     counter = 0
#     for i in range(n): # 0,1,2,3
#         for j in range(n): # 0,1,2,3
#             for t in range(n): # 0,1,2,3
#                 counter += 1
#                 print(i,j,t)

#     return counter


# print(print_numbers(2)) # O(8)
# print(print_numbers(3)) # O(27)
# print(print_numbers(4)) # O(64)

# # print(print_numbers(n)) = O(n^3) 


# --------------------------------------

# def print_numbers(n):
#     counter = 0
#     for i in range(n): # 0,1
#         for j in range(n): # 0,1
#             counter += 1

#     for t in range(n): # 0,1
#         counter += 1


#     return counter


# print(print_numbers(2)) # O(6)
# print(print_numbers(3)) # O(12)
# print(print_numbers(4)) # O(20)

# # # print(print_numbers(n)) = O(n^2+n)


# --------------------------------------
# # denklemi sadelestir

# # O(n^2+n) ~ n^2

# # Drop Constants - sabitleri atabilirsin
# # carpanlari atabiliriz.

# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         counter += 1
#         print(counter)

#     for i in range(n):
#         counter += 1
#         print(counter)


# print_numbers(10)
# # so in this example we do run the code n + n times: 2n
# # O(2n) and then we simplify the notation and drop the constant(sabit)
# # so we get O(n)


# # 3n^3 + n^2 + n ~= n^3
# # --> n^3+n^2+n


# --------------------------------------

# def add_items(n):
#     return n + n


# print(add_items(10))

# # T(n) = O(1)

# --------------------------------------

# def add_items(n):
#     return n + n + n


# print(add_items(10))

# # T(n) = O(1)

# --------------------------------------

# 1 < logn < n < nlogn < n^2,n^3,... < 2^n,3^n,... < n!

# --------------------------------------
# n^3 + 3n

# def multiple(n):
#     counter=0
#     for i in range(n):
#         for j in range(n):
#             for t in range(n):
#                 counter+=1
#     for z in range(n):
#         counter+=1
#     for y in range(n):
#         counter+=1
#     for f in range(n):
#         counter+=1
#     return counter
# print(multiple(2))


# --------------------------------------
# ODEV:

# 3n^3 + 3n + 5