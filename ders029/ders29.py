# # dunder method / magic mehtod

# class Toy:
#     def __init__(self,name,year,color):
#         self.name = name
#         self.year = year
#         self.color = color
#         self.my_dict = {
#             'name':'pixar',
#             'side_products':True
#         }

#     def __str__(self):
#         return f"{self.name=} -- {self.color=}"
    
#     def __len__(self):
#         return len(self.name)
    
#     def __call__(self):
#         return f"{self.name} cagirildi"
    
#     def __getitem__(self,key):
#         return self.my_dict.get(key)


# t1 = Toy('McQeen','2013','red')
# t2 = Toy('rainbow dash','2017','blue')
# print(t1.my_dict['name'])
# print(f"{len(t1)=}")

# print(t2.__str__())
# print(str(t2))
# print(t2)

# print(f"{len(t2)=}")

# print(t2.__call__())
# print(t2())

# print(t2.__getitem__('name'))
# print(t2[''])


# -----------------------------------
# # __new__

# class MyClass:
#     @classmethod
#     def from_name(cls,name):
#         obj = cls.__new__(cls) # bypass __init__
#         obj.name = name # set value to attribute directly
#         return obj


#     @classmethod
#     def from_age(cls,age):
#         obj = cls.__new__(cls)
#         obj.age = age
#         return obj
    

# obj1 = MyClass.from_age(20)
# obj2 = MyClass.from_name('berke')


# print(obj1)
# print(obj1.age)

# print(obj2)
# print(obj2.name)
# print(obj2.age) # error/ AttributeError

# -----------------------------------
# DRY : Dont Repeat Yourself

from dataclasses import dataclass,field

@dataclass
class Student:
    name: str
    surname: str
    age: int
    department: str

    # private
    __grade: float = field(repr=False)

    # ---- Encapsulation ----

    @property # getter
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self,new_grade):
        if 0<= new_grade <=100:
            self.__grade = new_grade
        else:
            print("Grade must be between 0 and 100")

    # ---- Encapsulation ----

    def __str__(self) -> int:
        return f"{self.name=} {self.surname=} {self.age=} {self.department=}"
    
    def __len__(self):
        return len(self.name + self.surname)
    
    def __eq__(self, other):
        return self.age == other.age


s1 = Student('berke','guducu',28,'software eng','98')
s2 = Student('yusuf','omoniddinov',28,'computer eng','99')
print(s1)
print(s1.name)
print(s1.age)
print(s1.grade) # 98
s1.grade = 100 # setter ile 100 yaptik
print(s1.grade) # sonuc olarak 100 aldik

print(id(s1))
print(id(s2))

print(s1 == s2)

print(len(s1)) # = print(s1.__len__())
print(len(s2))