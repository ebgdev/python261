# Error Handling

# print('123')
# print(1)


# print('hello' + ' berke') # concat
# # print('hello' + 123) # TypeError


# -----------------------------

# def deneme():
#     return 1


# print(deneme) # burada fonksiyon hakkinda bilgi almak istedikm, o yuzden kendisini yazdirdik
# print(deneme()) # burada fonksiyonu calistirdik


# -----------------------------


# def say_hello():
#     return 'hello' + berke # berke isimli degisken tanimli degil : NameError


# print(say_hello())

# ----------------------------

# nums = [11,12,13,14,15]

# print(nums[7]) # IndexError

# ----------------------------

# ogrenci = {'name':'berke','surname':'guducu','age':25}


# print(ogrenci['name'])
# print(ogrenci['is_married']) # KeyError


# ----------------------------

# print(10/0) # ZeroDivisionError


# ---------------------------------------------------------------------------------------------


# try Block:
#     # Code that may raise an exception is placed in a try block.
# except Block:
#     # This block catches and handles exceptions raised in the try block.
#     # You can catch specific exceptions or use a generic exception handler.
# else Block (Optional):
#     # Executes if no exceptions were raised in the try block.
# finally Block (Optional):
#     # Executes regardless of whether an exception was raised or not, typically used for cleanup.



# -----------------------------------------------------------------------------------------------

# age = int(input("what is your age? ")) # ValueError
# print(age) 



# try:
#     age = int(input("what is your age? "))
#     print(age)
# except:
#     print('please enter valid numbers')

# -----------

# hak_sayisi = 10
# deneme = 0
# while deneme < hak_sayisi:
#     try:
#         age = int(input("what is your age? "))
#         print(age)
#         break # break sadece try blogunun basarli oldugu senariyoda calisir
#     except:
#         print('please enter valid numbers')
#     print(f'deneme: {deneme+1}')
#     deneme += 1


# -----------

# while True:
#     try:
#         age = int(input("what is your age? "))
#         print(age)
#         break # break sadece try blogunun basarli oldugu senariyoda calisir
#     except:
#         print('please enter valid numbers')

# -----------------------------------------------------------------------------------------------

# while True:
#     try:
#         user_input = input("what is your age? (type exit to quit the program) ") # input: sayi, herhangi bir metin, exit
#         if user_input.lower() == 'exit': # '25'
#             print('Good Bye')
#             break
#         age = int(user_input)
#         print("Your age set successfully.")
#     except:
#         print('Enter a valid number')
#     else:
#         print('Thank you!!!')
#         break


# ------------------------------------------------------

while True:
    try:
        user_input = input("what is your age? (type exit to quit the program) ") # input: sayi, herhangi bir metin, exit
        if user_input.lower() == 'exit': # '25'
            print('Good Bye')
            break
        age = int(user_input)
        print("Your age set successfully.")
        print('Thank you!!!')
        break
    except:
        print('Enter a valid number')