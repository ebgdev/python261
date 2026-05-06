# class Toy:
# name,color,year,price
# nesne sayisi
# urettiginiz butun nesneleri bir listeye ekleyeceksiniz

class Toy:
    # class Object Attribute
    instance_count = 0
    lst = []
    def __init__(self,name,color,year,price):
        self.name = name
        self.color = color
        self.year = year
        self.price = price
        # obje burada olusuyor ve bitiyor
        # yani bu satirda obje elimde somut bir sekilde var
        Toy.instance_count += 1
        Toy.lst.append(self)

t1 = Toy('toy1','blue',2018,30)
t2 = Toy('toy2','red',2013,20)
t3 = Toy('toy3','blue',2015,10)
t4 = Toy('toy4','green',2020,40)
t5 = Toy('toy5','blue',2018,50)
t6 = Toy('toy6','white',2026,280)
t7 = Toy('toy7','red',2008,2)

# print(Toy.lst)
# print(len(Toy.lst))
# print(Toy.instance_count)


# print(t1) # <__main__.Toy object at 0x102491e80>
# print(t1.color)


# my_list = [
#     <__main__.Toy object at 0x1050f1e80>, <__main__.Toy object at 0x10509f390>, 
#     <__main__.Toy object at 0x10509f4d0>, <__main__.Toy object at 0x104fca190>, 
#     <__main__.Toy object at 0x104fc9e00>, <__main__.Toy object at 0x104f8ae70>, 
#     <__main__.Toy object at 0x105101370>
#     ]


def find_blues_name(lst):
    names = []
    for obj in lst:
        if obj.color.upper() == 'blue'.upper():
            names.append(obj.name)
    return names

print(find_blues_name(Toy.lst))


# --------------------------------------------------


def find_red_avg_year1(lst) -> float:
    year=0
    count=0
    for item in lst:
        if item.color == 'red':
            year += item.year
            count += 1
    return year/count

print(find_red_avg_year1(Toy.lst))



def find_red_avg_year2(lst) -> float:
    years = []
    for obj in lst:
        if obj.color == 'red':
            years.append(obj.year)
    return sum(years)/len(years)

print(find_red_avg_year2(Toy.lst))


from statistics import mean
def find_red_avg_year3(lst) -> float:
    years = [2013,2008]
    for obj in lst:
        if obj.color == 'red':
            years.append(obj.year)
    return mean(years)

print(find_red_avg_year3(Toy.lst))