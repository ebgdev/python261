# Keep asking until the user exits or guesses correctly.
# Kullanıcı çıkana veya doğru tahmin edene kadar döngü devam eder.

# import random

# memory_number = random.randint(0,100)


# print("To exit the program type 'exit'")

# while True:
#     predict_number = input("Predict number: ")
#     if predict_number == "exit":
#         print("You're exiting the program.")
#         break
#     predict_number = int(predict_number)
#     if predict_number == memory_number:
#         print("Dogru tahmin ettiniz")
#         break # donguyu kesmek icin
#     elif predict_number < memory_number:
#         print("Daha buyuk sayi tahmin ediniz")
#     else:
#         print("Daha kucuk sayi tahmin ediniz")


# ----------------------------------------

# If a function name starts with "is_", it is expected to return a boolean (True/False).
# Bir fonksiyon ismi "is_" ile başlıyorsa True/False (boolean) döndürmesi beklenir.
# # range(start, stop[, step])
# import time
# def is_prime(number):
#     counter = 0
#     for i in range(1,number+1): # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18
#         if number % i == 0:
#             counter+=1
#             # if counter > 2:
#             #     break
#     if counter == 2:
#         print(f"{number} is prime, and counter is {counter}")
#         return True
#     else:
#         print(f"{number} is not prime, and counter is {counter}")
#         return False


# t1 = time.time()
# print(is_prime(27644437))
# t2 = time.time()
# print(t2-t1)


# --------------------------------------------------

# def is_prime(number):
#     counter = 0
#     for i in range(2,number): # 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
#         if number % i == 0:
#             counter+=1
#             if counter > 2:
#                 break
#     if counter == 0:
#         # print(f"{number} is prime, and counter is {counter}")
#         return True
#     else:
#         # print(f"{number} is not prime, and counter is {counter}")
#         return False


# print(is_prime(18))
# print(is_prime(17))


# --------------------------------------------------
# import time
# import math
# def is_prime(number):
#     counter = 0
#     for i in range(2,int(math.sqrt(number))+1): # 2,3,4
#         if number % i == 0:
#             counter+=1
#             if counter > 0:
#                 break
#     if counter == 0:
#         # print(f"{number} is prime, and counter is {counter}")
#         return True
#     else:
#         # print(f"{number} is not prime, and counter is {counter}")
#         return False


# t1 = time.time()
# print(is_prime(27644437))
# t2 = time.time()
# print(t2-t1)
# # # print(is_prime(17))
# # # print(is_prime(25))


# --------------------------------------------------
# Write a function that finds the length of a list without using the built-in len() function.
# Hazır len() fonksiyonunu kullanmadan listenin uzunluğunu bulan bir fonksiyon yazınız.

ogrenciler1 = ['berat','berke','damla','aynaz','erfan']
ogrenciler2 = ['berat','berke','damla','aynaz','erfan','furkan',"cem","feyza"]

def custom_len(liste):
    counter = 0
    for _ in liste:
        counter += 1
    return counter


print(custom_len(ogrenciler1)) # 5
print(custom_len(ogrenciler2)) # 8
