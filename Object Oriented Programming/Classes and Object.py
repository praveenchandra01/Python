class Test:
    i=10
    def f1():
        print("Hello")
print(Test.i) #class object
Test.f1()    #instance object
        
class Test:
    def __init__(self):
        print("init")
t1=Test()        
        
class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
t1=Test(3 ,4)        
print(t1.a,t1.b)        


class Test:
    def __init__(self,x,y):
        self.a=x
        self.b=y
t1=Test(1 ,4)
t2=Test(50,100)
t3=Test(6,9)
print(t1.a,t1.b)
print(t2.a,t2.b)
print(t3.a,t3.b)   
