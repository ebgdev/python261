# OOP : Object Oriented Programming


# class PlayerCharacter():
#     # class object attribute
#     isinstance_counter = 0

#     # initializer method
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         PlayerCharacter.isinstance_counter += 1

#     # instance method
#     def run(self):
#         return f"{self.name} can run"
    

# player1 = PlayerCharacter('zeus',41)
# player2 = PlayerCharacter('hades',1000)
# print(player1)
# print(type(player1))
# print(PlayerCharacter.isinstance_counter)

# print(player2.name)
# -----------------------------------------------------

# from datetime import datetime
# import uuid

# class Toyota():
#     instance_counter = 0
#     def __init__(self,model,color):
#         self.model = model
#         self.year = datetime.now().year
#         self.chassis_no = uuid.uuid4()
#         self.color = color
#         Toyota.instance_counter += 1
    
#     # instance method
#     def print_info(self):
#         return f"{self.model} - {self.year} - {self.chassis_no} - {self.color}"
    
#     def slogan():
#         return "Let's go Places"
    

# toyota1 = Toyota('corolla','blue')
# toyota2 = Toyota('land crusiour','black')
# toyota3 = Toyota('yaris','green')
# toyota4 = Toyota('camary','red')

# print(toyota1.print_info())
# # print(toyota1.slogan()) ❌
# # print(Toyota.slogan()) ✅
# # print(Toyota.print_info()) ❌
# print(Toyota.instance_counter)


# -----------------------------------------------------
# classmethod

# from datetime import datetime

# class Person():
#     instance_counter = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Person.instance_counter +=1
    
#     @classmethod
#     def get_with_str(cls,astr):
#         current_year = datetime.now().year
#         name, year = astr.split('-')
#         age = current_year - int(year)
#         return cls(name,age)
    
#     @staticmethod # odev ?
#     def foo():
#         pass

# str1 = "meltem-2003"

# person1 = Person('berke',25)
# person2 = Person.get_with_str(str1)

# print(person2.name)
# print(person2.age)

# print(f"{Person.instance_counter=}")



# -----------------------------------------------------

# str1 = "meltem-gemalmaz"

# init: self.name, self.surname


class Person():
    instance_counter = 0
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        Person.instance_counter +=1
    
    @classmethod
    def get_with_str(cls,astr):
        name, surname = astr.split('--') # split function return value always is an array
        return cls(name,surname)


person1 = Person.get_with_str('berke--guducu')
person2 = Person.get_with_str('yusuf--omonidinov')


print(person1.name,person1.surname)
print(person2.name,person2.surname)

print(Person.instance_counter)