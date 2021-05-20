class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show_Name(self):
        print("Name :",self.name)
    def show_Age(self):
        print("Age :",self.age)

class Student(Person):
    def __init__(self,r,n,a):
        super().__init__(n,a)      #self implicitly pass
        '''Person.__init__(self,"Rahul",19)''' 
        self.rollno=r
        '''Person.__init__(self,"Rahul",19)''' #This will also run
    def show_Roll(self):
        print("Roll no :",self.rollno)
S1=Student(100,"Rahul",19)
S1.show_Roll()
S1.show_Name()
S1.show_Age()
        
