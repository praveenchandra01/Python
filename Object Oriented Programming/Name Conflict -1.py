#Instence Member variable name conflict
class Base:
    def __init__(self):
        self.a=10
    def showBase(self):
            print("Base a=",self.a)
class Derived(Base):
    def __init__(self):
         #self.a=20 
        super().__init__()
        self.a=20
    def showDerived(self):
        print("Derived a=",self.a)
obj=Derived()
obj.showBase()
obj.showDerived()

#Static member function name conflict
print("*****Static Variable*****")
class Base:
    x=11
    def __init__(self):
        self.a=10
        Base.x=13
    def showBase(self):
            print("Base a=",self.a)
class Derived(Base):
    x=12
    def __init__(self):
        super().__init__()
        self.a=20
    def showDerived(self):
        print("Derived a=",self.a)
print(Base.x)        
obj=Derived()
print("After Base.x=13 :",Base.x) 
print(Derived.x)
print("Base :",Base.x,"Derived :",Derived.x)
