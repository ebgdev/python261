# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.__balance = balance

#     def deposite(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f'deposited {amount}. The balance is now {self.__balance}')
#         else:
#             print('deposite amount should be a positive value')
    
#     # faiz ekleme fonksiyonu - private instance method
#     def __apply_intereset(self):
#         # %2 faiz uygulayalim
#         self.__balance *= 1.02
#         return self.__balance
    
#     def get_balance(self):
#         self.__apply_intereset()
#         return self.__balance


# account = BankAccount('erfan',1000)
# account.deposite(2000)
# print(account.get_balance())


# ------------------------------------------------------------

# class Parent():
#     pass


# class Child(Parent):
#     pass

# parent1 = Parent()
# child1 = Child()
# print(child1)

# print(isinstance(child1,Child)) # nesnesi mi ?
# print(isinstance(child1,Parent)) # nesnesi mi ?
# print(isinstance(parent1,Parent)) # nesnesi mi ?
# print(isinstance(parent1,Child)) # nesnesi mi ?


# print(issubclass(Parent,Child)) # parent childin bir alt sinifi midir ?
# print(issubclass(Child,Parent)) # parent childin bir alt sinifi midir ?


# ------------------------------------------------------------

# # Çok Biçimlilik (Polymorphism)

# class User():
#     def sign_up(self):
#         return "signed up"
    
#     def konus(self):
#         return(f"User sinifindan uretilen obje konusuyor")


# class Ogrenci(User):
#     def __init__(self,name):
#         self.name = name
    
#     def konus(self):
#         return(f"Ogrenci sinifindan uretilen obje konusuyor")


# class Ogretmen(User):
#     def __init__(self,name):
#         self.name = name

#     def konus(self):
#         return super().konus()


# user1 = User()
# print(user1.konus())

# ogrenci1 = Ogrenci('yusuf')
# print(ogrenci1.konus())

# ogretmen1 = Ogretmen('erfan')
# print(ogretmen1.konus())

# ------------------------------------------------------------

# dunder method, magic methodlari


class Toy:
    def __init__(self,name,color,speakable):
        self.name = name
        self.color = color
        self.speakable = speakable

    def __str__(self):
        return f'{self.name} -- {self.color}'

    

toy1 = Toy('McQueen','red',True)
toy2 = Toy('captin america','white/blue','True')
# print(dir(toy1))
print(toy1)
print(id(toy1))
print(id(toy2))


# ODEV:

# __repr__ nedir ? 
# __repr__ ve __str__ arasindaki fark nedir ?
# __len__ ne ise yarar ?
# __call__ ne ise yarar ?