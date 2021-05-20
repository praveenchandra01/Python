class Test:
    x=10  #static var accessible outside the class
    __h=20 #static Hidden variable
    
    def __init__(self):
        self.__a=100
        
    @staticmethod
    def f1():
        print("Inside class",Test.__h)
        
obj=Test()
print(obj.__dict__)
Test.f1()
print(Test.x)
print("Print outside the class ",Test._Test__h)
