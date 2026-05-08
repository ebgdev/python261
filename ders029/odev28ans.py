from statistics import mean


class Toy():
    instance_count = 0
    instances = []
    def __init__(self,name,color,year,price):
        self.name = name
        self.color = color
        self.year = year
        self.price = price
        Toy.instance_count += 1
        Toy.instances.append(self)



t1 = Toy('toy1','blue',2018,30)
t2 = Toy('toy2','red',2013,20)
t3 = Toy('toy3','blue',2015,10)
t4 = Toy('toy4','green',2020,40)
t5 = Toy('toy5','blue',2018,50)
t6 = Toy('toy6','white',2026,280)
t7 = Toy('toy7','red',2008,2)

def find_color_not_blue_red_avg_price(lst) -> float:
    prices = []
    for obj in lst:
        if obj.color not in ('blue','red'):
            prices.append(obj.price)
    return mean(prices)

print(find_color_not_blue_red_avg_price(Toy.instances))



def find_color_not_blue_red_avg_price(lst) -> float:
    total_price = 0
    obj_count = 0
    for obj in lst:
        if obj.color != 'red' and obj.color != 'blue':
            total_price += obj.price
            obj_count += 1
    return total_price/obj_count

print(find_color_not_blue_red_avg_price(Toy.instances))
print(find_color_not_blue_red_avg_price)