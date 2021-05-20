class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
        
class Student(Person):
    def __init__(self,n,a,r):
        self.Rollno=r
        Person.__init__(self,n,a)
        
class Teacher(Person):
    def __init__(self,n,a,sal,sub):
        self.Salary=sal
        self.Subject=sub
        Person.__init__(self,n,a)
        
class BrightStudent(Student,Teacher):
    def __init__(self,n,a,r,sal,sub,p):
        self.Points=p
        Student.__init__(self,n,a,r)
        Teacher.__init__(self,n,a,sal,sub)

obj=BrightStudent("Preveen",19,13075,35000,"DBMS",7)        
print(obj.__dict__)

