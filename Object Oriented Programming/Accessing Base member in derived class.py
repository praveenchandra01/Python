#Instance member variable of base class in derived class
class Base:
    def __init__(self):
        self.a=10
class Derived(Base):
    def __init(self):
        super().__init__()
    def f1(self):
        print(self.a)
obj=Derived()
obj.f1()

#Static memeber variable of base class in derived class
class Base:
    x=11 #static variable
    def __init__(self):
        self.a=10
class Derived(Base):
    def __init(self):
        super().__init__()
    @staticmethod    
    def f1():
        print(Derived.x)
Derived.f1()

 #Instance member function of base class in derived class
class Base:
    def __init__(self):
        self.a=10
    def basefunction(self):
        print("Base Instace function a=",self.a)
class Derived(Base):
    def __init__(self):
        super().__init__()
    def f1(self):
        self.basefunction()
        super().basefunction()
obj=Derived()
obj.f1()

#static memeber function of base class in derived class
class Base:
    x=101 #static variable
    def __init__(self):
        self.a=10
    @staticmethod   
    def basefunction():
        print("Base Instace function x=",Base.x)
class Derived(Base):
    def __init__(self):
        super().__init__()
    def f(self):
        super().basefunction()  
    @staticmethod    
    def f1():
        Base.basefunction()
Derived.basefunction()
obj=Derived()
obj.f1()
