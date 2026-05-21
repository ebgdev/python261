# ODEV: Asagidaki kodu dataclass'ler ile yapiniz
# Dataclass'ler ile yapin, Field kullanrak bu kodu yaziniz.
# Person : first_name,last_name,user_name,id
from uuid import uuid4

class Person():
    def __init__(self,first_name,last_name,user_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.__id = uuid4().hex

    def __str__(self):
        return self.user_name

p1 = Person('berke','guducu','brkG')
print(p1)
p2 = Person('yusuf','omoniddinov','yusuf_uz')
print(p2)
