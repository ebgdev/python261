# class Car:

#     # class object attribute
#     all_objects = []
#     def __init__(self, factory, model, engine, seat, door, Vtype):
#         self.factory = factory
#         self.model = model
#         self.engine = engine
#         self.seat = seat
#         self.door = door
#         self.Vtype = Vtype
#         # burada obje olusturuldu
#         Car.all_objects.append(self)

#     # pre-processing - on-isleme
#     @classmethod
#     def get_with_arr(cls,arr):
#         factory,model,engine,seat,door,Vtype = arr
#         return cls(factory,model,engine,seat,door,Vtype)

# # \n --> line feed
# with open("odev33info.txt") as f:
#     for line in f:
#         line = line.strip('\n')
#         Car.get_with_arr(line.split(','))


# print(Car.all_objects[9].model)


# -----------------------------------------------------

# all_objects = {car1:0x102528500,car2:0x102528500}


class Car:

    # class object attribute
    all_objects = {}
    c = 1
    def __init__(self, factory, model, engine, seat, door, Vtype):
        self.factory = factory
        self.model = model
        self.engine = engine
        self.seat = seat
        self.door = door
        self.Vtype = Vtype
        # burada obje olusturuldu
        Car.all_objects[f'car{Car.c}'] = self
        Car.c += 1

    # pre-processing - on-isleme
    @classmethod
    def get_with_arr(cls,arr):
        factory,model,engine,seat,door,Vtype = arr
        return cls(factory,model,engine,seat,door,Vtype)

# \n --> line feed
with open("odev33info.txt") as f:
    for line in f:
        line = line.strip('\n')
        Car.get_with_arr(line.split(','))


objects = Car.all_objects
print(objects['car12'].model)