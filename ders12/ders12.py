# # TEMIZ KOD DEGIL ❌
# # KENDIMIZI TEKRARLIYORUZ


# pass1 = input("Enter your first password: ")
# pass2 = input("Enter your second password: ")

# if pass1 == pass2 and pass1 != "": # ... and not pass1 
#     print("Congrats, password set successfully.")

# while pass1 != pass2 or pass1 == "":
#     print("try again")
#     pass1 = input("Enter your first password: ")
#     pass2 = input("Enter your second password: ")

#     if pass1 == pass2 and pass1 != "": # ... and not pass1 
#         print("Congrats, password set successfully.")
#         break


# ------------------------------------------------------

# for i in range(10): # 0-9
#     if i == 5:
#         continue # donguye kaldigin yerden devam et.
#     print(i)

# ------------------------------------------------------
# # DAHA TEMIZ KOD ✅
# # TEKRAR KOD YOK ✅
# # DRY: “Don't repeat yourself”

# while True:
#     pass1 = input("Enter your password: ")
#     pass2 = input("Confirm your password: ")

#     if not pass1 or not pass2:
#         print("Passwords cannot be blank.\n")
#         continue

#     if pass1 != pass2:
#         print("Passwords do not match. Try again.\n")
#         continue

#     if len(pass1) < 8:
#         print("Password must be at least 8 characters long.\n")
#         continue
    
#     print("Congrats, password set successfully!")
#     break


# -------------------------fibo---------------------------

# new_element = fibo[3]+fibo[4]
# print(new_element)


def find_fibo(n):
    fibo = [0,1]
    if n <= 0:
        return []
    if n == 1:
        return [0,1,1]
    
    for _ in range(n):
        # son eleman ile , son bir kalan elamni topla , fiboya yeni elaman olarak ekle
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

print(find_fibo(-10))
print(find_fibo(0))
print(find_fibo(1))
print(find_fibo(2))
print(find_fibo(10))
