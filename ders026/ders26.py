# class Apple:
#     def __init__(self,model):
#         # attribute = parameter
#         self.model = model

#     # instance method
#     def print_info(self):
#         return f"apple object model is: {self.model}"

#     @staticmethod
#     def about_apple():
#         return "think different"




# iphone = Apple('iphone 4') # ornekleme/nesne uretimi/instanciation
# print(iphone.print_info())
# # print(Apple.print_info()) Error
# print(iphone.about_apple())
# print(Apple.about_apple())

# print(iphone.model)


# ------------------------------------------------------

# OOP:
# Soyutlama (Abstraction)
# Kapsülleme (Encapsulation)
# Miras Alma (Inheritance)
# Çok Biçimlilik (Polymorphism)

# ------------------------------------------------------

# class PlayCharacter():
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname


# player1 = PlayCharacter('berke','guducu')
# print(player1.name)
# player1.name = 'yusuf' # erisim izni var, erisip ismi degistirebiliyoruz

# print(player1.name,player1.surname)


# --------------------encapsulation----------------------

#####################-information-#####################

# public    = variable (Fully accessible from anywhere)
# protected = _variable (Is for developers to know should only access inside class or subclass) still allows so not enfored.
# private   =  __variable (is to prevent from accidential access ) outside of class: only accessible with special method.

# --------------------------getter-and-setters-------------------------


# class Person():
#     def __init__(self,name,age):
#         # attribute - attr
#         self.__name = name
#         self.__age = age
#     # read
#     def name_getter(self):
#         return self.__name
#     # read
#     def age_getter(self):
#         return self.__age
#     # write
#     def age_setter(self,new_age):
#         self.__age = new_age
    
#     # write
#     def name_setter(self,new_name):
#         self.__name = new_name



# person1 = Person('yusuf',21)
# print(person1.name_getter())
# person1.name_setter('emre')
# print(person1.name_getter())
# print(person1.age_getter())
# person1.age_setter(22) # write
# print(person1.age_getter()) # read
# # print(person1.__name) # Error
# # print(person1.__age) # Error


# ---------------------------------------------------------

# Miras Alma (Inheritance)
# DRY kodlama
import uuid

class Employee:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        # hidden attributes
        self.id = uuid.uuid4()


class Student(Employee):
    def __init__(self, name, surname,age,class_no,gender):
        super().__init__(name, surname)
        self.age = age
        self.class_no = class_no
        self.gender = gender


class Teacher(Employee):
    def __init__(self, name, surname,lectures):
        Employee.__init__(self,name, surname)
        # name_surname@school.com
        # hidden attribute
        self.email = f'{self.name}_{self.surname}@school.com'
        self.lectures = lectures


em1 = Employee('efe','tufekci')
t1 = Teacher('erfan','bahcivan',['python','postgresql'])
print(t1.id)
print(t1.email)
print(t1.lectures)
