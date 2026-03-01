# local
# global

# y = 10

# def modify_global():
#     y = 20
#     return y


# print(modify_global())
# print(y)

# --------------------------------------

# y = 10 # 20

# def modify_global():
#     global y
#     y = 20
#     return y


# print(modify_global())
# print(y)

# --------------------------------------
# Bir variable ayni zamanda hem non-local hem global yapilamaz.

# z = 100 
# def outer_function():
#     z = 10  # z is a local variable in outer_function # 40

#     def inner_function():
#         nonlocal z  # z is treated as nonlocal in inner_function
#         z = 40
#         print(f"Inside inner_function, z = {z}")

#     inner_function()
#     print(f"Inside outer_function, z = {z}")

# outer_function()


# print(z)


# --------------------------------------

# # Global variable
# x = 10 # 40

# def outer_function():
#     # Local variable in outer_function
#     local_x = 20 # 30
    
#     def inner_function():
#         # Modify the local variable of outer_function
#         nonlocal local_x
#         local_x = 30
#         print(f"Inside inner_function, nonlocal x = {local_x}")
        
#         # Modify the global variable
#         global x
#         x = 40
#         print(f"Inside inner_function, global x = {x}")

#     inner_function()
#     print(f"Inside outer_function, after calling inner_function, nonlocal x = {local_x}")

# outer_function()
# print(f"Outside, global x = {x}")


# --------------------------------------

# my_list = ['elma']
# my_tuple = ('elma',)
# my_tuple1 = ('elma')

# print(type(my_tuple1))
# print(type(my_tuple)) 


# --------------------------------------

# a = [1,2,3,4,5,6,7,8,9,10]
# # b = [2,4,6,8,10,12,16,18,20]

# b = []
# for item in a:
#     b.append(item*2)
# print(b)


# ---------------------------------------

# # anonymous function
# # isimsiz fonksiyon
# def add_ten(x):
#     return x + 10

# add_ten_plus = lambda x : x + 10

# print(add_ten(5))
# print(type(add_ten_plus))
# print(add_ten_plus(55))

# ---------------------------------------

# print((lambda x: x+10)(55))

# print((lambda x: x*10)(10))


# ---------------------------------------

a = [1,2,3,4,5,6,7,8,9,10]

# multiply_with_ten = ((lambda x:x*10)(x)for x in a)
# # print(multiply_with_ten)

# for item in multiply_with_ten:
#     print(item)


# ------------------------

add_three = ((lambda x: x+3)(x)for x in a)
for item in add_three:
    print(item)