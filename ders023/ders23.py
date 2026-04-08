# # class names should be PascalCase
# # OOP : Object Oriented Programming : Nesne Yonelimli Programlama
# class Car:
#     # initializer method, constructor method, yapici method
#     def __init__(self,manufactor,engine,model,year,door,wheel):
#         # attribute  =  argument (varible)
#         self.manufactor = manufactor
#         self.engine = engine
#         self.model = model
#         self.year = year
#         self.door = door
#         self.wheel = wheel

#     # instance/object method
#     def print_info(self): # self = egea
#         return f"manufator: {self.manufactor} - engine: {self.engine} - model: {self.model} - year: {self.year}"


# # ram: random access memory

# # instance
# corolla = Car("Toyota","1,6","corolla","2024","4","4")
# egea = Car("Fiat","1.4","egea","2025","4","4")




# print(egea.print_info())


# ---------------------------------------------

# # more info : https://en.wikipedia.org/wiki/History_of_programming_languages

# # # everything in python is object
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(3.3))
# print(type("hi"))
# print(type([]))
# print(type(()))
# print(type({}))



# ----------------------------------------------

# iki sinif : Kedi, Kopek

# def speak

# leo = Kedi()
# leo.speak() --> Meoww



# milo = Kopek()
# milo.speak() --> Hav Hav


# ----------------------------------------------


class Cat:
    def __init__(self):
        pass

    def speak(self):
        return "Meoww"


class Dog:
    def __init__(self):
        pass
    def speak(self):
        return "Hav Hav"
    
# name = "erfan" # assign value # deger atama


leo = Cat() # instanciate # ornekleme
print(leo.speak())

milo = Dog()
print(milo.speak())