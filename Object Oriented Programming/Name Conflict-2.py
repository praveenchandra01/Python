#Instance Member Function name Conflict
class Base:
    def __init__(self):
        self.a=10
    def f1(self):
        print("Base f1")
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.a=20
    def f1(self):   #overriding
        print("Derived f1")
        super().f1()  #calling function in parent class
obj=Derived()
obj.f1()

#Static Member Function
class Base:
    def f1():
        print("Base f1")
class Derived:
    def f1():
        Base.f1()
        print("Derived f1")
        
Derived.f1()        
