# my_list = ['berke','meltem','yusuf','ali','omer','faruk']


# # enumerate
# tekli_indeksler = []
# cifli_indeksler = []

# for index,item in enumerate(my_list):
#     if index % 2 == 0:
#         cifli_indeksler.append(item)
#     else:
#         tekli_indeksler.append(item)

# print(tekli_indeksler,cifli_indeksler)


# ------------------------------------------

# lst = [11,13,14,28,123,65,2,-1,0]

# def is_prime(num:int) -> bool:
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True


# # print(is_prime(-1)) # True

# for item in lst:
#     print(f'{item}:{is_prime(item)}')


# ------------------------------------------
# from uuid import uuid4

# class Person():
#     def __init__(self,first_name,last_name,user_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.user_name = user_name
#         self.id = uuid4().hex

#     def __str__(self):
#         return self.user_name
    
#     def __call__(self):
#         return self.id


# p1 = Person('berke','guducu','brkG')
# # print(p1)
# p2 = Person('yusuf','omoniddinov','yusuf_uz')
# # print(p2)

# # print(p1.__call__())
# # print(p1())

# p1.first_name = 'G'
# print(p1)

# ----------------------------------------------------------------


from uuid import uuid4

class Person():
    def __init__(self,first_name,last_name,user_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.__id = uuid4().hex

    # instance method
    def id(self):
        return self.__id

    def id_setter(self,new_id):
        self.__id = new_id

    def __str__(self):
        return self.user_name

p1 = Person('berke','guducu','brkG')
# print(p1)
p2 = Person('yusuf','omoniddinov','yusuf_uz')
# print(p2)

# print(p1.__call__())
# print(p1())

p1.first_name = 'G'
print(p1.id())
p1.id_setter(1)
print(p1.id())

p1.id = 100
print(p1.id)

print(p2.id())