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


def find_color_not_blue_red_avg_price(lst):
    prices = []
    pass