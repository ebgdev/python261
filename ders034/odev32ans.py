# Bu sinifi dataclass ile yapacagiz.
from dataclasses import dataclass,field
from uuid import uuid4

@dataclass
class Person():
        first_name : str
        last_name : str
        user_name : str
        __id : int = field(repr=False)

        # ------ encapsulation --------
        @property # getter
        def id(self):
            return self.__id
        
        @id.setter
        def id(self,new_id):
            self.__id = new_id

        # ------ encapsulation --------

    # def __str__(self):
    #     return self.user_name

p1 = Person('berke','guducu','brkG',1)
print(p1.id)
p1.id = 3
print(p1.id)
print(id(p1))