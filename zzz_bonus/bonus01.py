import random


# # 1.yontem:
# hak_sayisi = 5
# while hak_sayisi > 0:
#     print(random.randint(1,100))
#     hak_sayisi -= 1



# # 2.yontem:
# hak_sayisi = 5
# while True:
#     if hak_sayisi == 0:
#         break
#     print(random.randint(1,100))
#     hak_sayisi -= 1


# # 3.yontem:
# hak_sayisi = 5
# for x in range(hak_sayisi): # 0,1,2,3,4
#     print(random.randint(1,100))



# -------------------------------------------------

# 100 gelmedigi surece calistir
# kac denemede 100 degerine ulastigini don

# def generate_till_n(n,a,b):
#     counter = 0
#     kosul = True
#     while kosul:
#         counter += 1
#         random_number = random.randint(a,b)
#         print(f"{counter=},{random_number=}")
        
#         if random_number == n:
#             kosul = False
#     return counter


# print(generate_till_n(100,1,100))


# ------------------------------------------------


def generate_till_n(n:int,a:int,b:int):
    """
    n is value that are we looking for.
    a is a starting point which is included
    b is end point which is included too.
    """
    counter = 0
    while True:
        counter += 1
        random_number = random.randint(a,b)
        print(f"{counter=},{random_number=}")
        
        if random_number == n:
            break
    return counter


print(generate_till_n(8,1,100))