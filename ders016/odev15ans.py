import math
new_array = [i for i in range(1,101)]
# print(new_array)
# Elimizde 1 den 100 kadar bir liste olsun
# filter ile nasil sadece asal sayilari secebilirim ?

# ipucu 
# filter(function,iterable)
# bize bir fonksiyon gerek, liste belli
# bu fonksiyonu biz olusturabilir miyiz ?

# -----------------cozum---------------

# iterable : uzerinden dongu ile dolasabilecegim seyler.
# or: str,list,tuple,generators

# -------------------
# # generator object ornegi:
# sayilar = [1, 2, 3, 4, 5, 6]
# sayilar_kare = ((lambda x: x**2)(x)for x in sayilar)
# print(f"{sayilar_kare=}")

# for sayi in sayilar_kare:
#     print(sayi)
# ---------------------

def is_prime(num) -> bool:
    if num <= 1:
        return False
    for i in range(2,(num//2)+1):
        if num % i == 0:
            return False
    return True

prime_numbers = list(filter(is_prime,new_array))
print(prime_numbers)


# ----------------------
# import math

# new_array = [i for i in range(1,101)]

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2,(number//2)+1):
#         if number % i == 0:
#             return False
#     return True


# primes = list(filter(lambda x: is_prime(x),new_array))
# print(primes)