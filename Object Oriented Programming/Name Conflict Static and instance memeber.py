#Between Static Variable and instance variable
class Base:
    x=10
    def __init__(self):
        self.x=20
class Derived:
    def __init__(self):
        super().__init__()
obj=Derived()
print(obj.x,Derived.x)
#Between Static member and instane member
class Base:
    def __init__(self):
        print("First instance")
    def __init__(self,x):
        print("Second instance")
    @staticmethod
    def f1():
        print("Static F1")
    def f1(self):
        print("Instance F1")
obj=Base(2)
#Base.f1()
