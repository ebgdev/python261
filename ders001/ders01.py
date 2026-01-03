# # tam sayi - integer
# x = 3
# print(type(x))

# # nokta virgulu sayilar, kayar nokatali sayilar , float point numbers
# y = 3.14
# print(type(y))

# # karakter - string
# name = 'erfan'
# print(type(name))

# Boolean tipleri - Boolean types
# True
# False

# None Type
# None

# -----------------------------
# # operator

# x = 10
# y = 5

# print(x+y)
# print(y-x)
# print(x*y)
# print(x/y)
# print(y**x) # y uzere x -> 5^10
# print(5/4) # float
# print(9//4) # int (asagi dogru yuvarlar)
# # print('x*2*y')

# print(3 == '3')
# print(3 == 3.0)

# print(type(3 == '3'))
# print(type(3 == 3.0))
# print(x >= y)
# print(x<=y)
# print(3 != '3')
# print(not True)
# print(not False)


# -------- concatenate - birlestirme ----------

# # (variable --tr--> degisken)
# name = 'erfan'
# surname = 'bahcivan'


# print(name + ' ' + surname)
# print(name + 10) # TypeError aliriz : can only concatenate str (not "int") to str
# print(13+3.14)

# ----------------------------------------------
# if - else blogu
name = 'erfan'


if name == 'erfan':
    print("merhaba sisteme hosgeldiniz")
else:
    print("maalesef sisteme giris yapamazsiniz")