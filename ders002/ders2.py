# name = 'erfan"s book'
# name2 = "erfan's book"

# print(name)
# print(name2)

# --------------------------

# name = input("Enter your name: ")
# print("merhaba",name)

# --------------------------

## kosul/sart --en--> condition(True, False)
## eger kosul dogruysa (True) iceri girer ve code calisir
## ** Dikkat: her if gordugumuz yerde yeni block baslar.

# if condition:
#   run the code
# elif condition:
#   run the code
# elif condition:
#   run the code
# else:
#   otherwise this code will run 



# --------------------------

# # input fonksiyonu her zaman veriyi str cinsinden alir.
# age = int(input('please enter your age: ')) 

# # print(type(age))

# if age >= 18:
#     print("hosgeldin")
# else:
#     print("giremezsin")


# --------------------------
# # if yazdigimiz yerde yeni if/else blogu baslar. ✅
# sehir = "trabzon"

# if sehir == "samsun":
#     print(55)
# elif sehir == "istanbul":
#     print(34)
# elif sehir == "bursa":
#     print(16)
# elif sehir == "trabzon":
#     sehir = "ankara"
# else:
#     print("sehir bilinmiyor")

# print(sehir)


# ----------------------------------

# sehir = "istanbul"

# if sehir == "samsun":
#     sehir = "istanbul"
#     print(55)
# elif sehir == "istanbul":
#     sehir = "bursa"
#     print(34)


# if sehir == "bursa":
#     sehir = "trabzon"
#     print(16)
# elif sehir == "trabzon":
#     sehir = "ankara"
#     print('06')
# else:
#     print("sehir bilinmiyor")

# print(sehir)


# if sehir == "trabzon":
#     sehir = "izmir"
#     print(61)
# elif sehir == "izmir":
#     sehir = "tokat"
#     print(35)
# else:
#     "gule gule"

# print(sehir)


# ----------------------------------

# sehir = "trabzon"

# if sehir == "samsun":
#     print("55")
#     sehir = "trabzon"
# elif sehir == "trabzon":
#     print("61")
#     sehir = "adana"
# elif sehir == "adana":
#     print("01")
#     sehir = "izmir"
# else:
#     print("sehir bulunamadi.")

# print("sehirin son durumu: ",sehir)


# ----------------------------------
# terminal/ kullanicidan,user / veri alacagiz --> input
# input
    # numeric
    # str

# Modulo (Modulus) operatörü: %
# % : 5 % 2 --> 5 bolu 2 kalani ne olur ?


number = int(input("Enter a number: "))

if number % 2 == 0:
    print("number is even.")
else:
    print("number is odd.")