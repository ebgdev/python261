# odemeler = ['200','30.5','120','30.2','100']

# ----------------------------------

# # yontem1: normal for
# def find_min_number(lst):
#     temp_min = float('inf') # max icin ise float('-inf')
#     for num in lst:
#         if float(num) < temp_min:
#             temp_min = float(num)
#     return temp_min



# # yontem2: for range ile
# def find_min_number(lst):
#     temp_min = float(lst[0]) # max icin ise float('-inf')
#     for index in range(1,len(lst)):
#         if float(lst[index]) < temp_min:
#             temp_min = float(lst[index])
#     return temp_min



# # yontem3: while ile
# def find_min_number(lst):
#     temp_min = float(lst[0]) # max icin ise float('-inf')
#     index = 1
#     while index < len(lst):
#         if float(lst[index]) < temp_min:
#             temp_min = float(lst[index])
#         index += 1
#     return temp_min


# # yontem 4.1: enumerate() ile, item kullandik (normal for dongusune benzedi)
# def find_min_number(lst):
#     temp_min = float(lst[0]) # max icin ise float('-inf')
#     for index, item in enumerate(lst):
#         if float(item) < temp_min:
#             temp_min = float(item)
#     return temp_min


# yontem 4.2: enumerate() ile, index kullandik (for i in range dongusune benzedi)
# def find_min_number(lst):
#     temp_min = float(lst[0]) # max icin ise float('-inf')
#     for index, item in enumerate(lst):
#         if float(lst[index]) < temp_min:
#             temp_min = float(lst[index])
#     return temp_min



# print(find_min_number(lst=odemeler))
# print(find_min_number(lst=harclar))


# ----------------------------------------------------------
# harclar = ['20','300','12','70','1','18']

# def find_max_number(lst):
#     temp_max = int(lst[0]) # 20
#     index = 1
#     while index < len(lst): # 1,2,3,4,5
#         if int(lst[index]) > temp_max:
#             temp_max = int(lst[index])
#         index += 1
#     return temp_max


# print(find_max_number(harclar))



# --------------------------------------------------------------------------
# odemelerin ortalamasi nedir ? 
# tercihen while ile yapiniz

# -------------------------------------

# odemeler = ['200','30.5','120','30.2','100']

# def find_avg_payments_str(lst):
#     index = 0
#     total = 0
#     while index < len(lst):
#         total += float(lst[index])
#         index += 1
#     return total/len(lst)

# print(find_avg_payments_str(lst=odemeler))

# -------------------------------------

# odemeler1 = [200,30.5,120,300,30.2,100]

# def find_avg_payments(lst):
#     size = len(lst)
#     total = sum(lst)
#     return total/size


# print(find_avg_payments(odemeler1))
# print(max(odemeler1))
# print(min(odemeler1))


# -------------------------------------

# range syntax
# range(start, stop[, step])


# for i in range(2,21,3): # 2,5,8,11,14,17,20
#     print(i)


# for i in range(2,20,3): # 2,5,8,11,14,17
#     print(i)


# range(3,13,2) : 3,5,7,9,11

for i in range(3,13,2):
    print(i)