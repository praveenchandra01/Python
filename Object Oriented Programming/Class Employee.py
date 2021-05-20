class Employee:
    def __init__(self,x,y,z):
        self.name=x
        self.emid=y
        self.salary=z
    def Display(self):
        print("Employee Data :")
        print("Employee Name :",self.name)
        print("Employee id :",self.emid)
        print("Employee Salary :",self.salary)
        
n=input( "Enter Employee Name :")
a=int(input("Enter Employee id :"))
b=int(input("Enter Employee Salary :"))
E1=Employee(n,a,b)
E1.Display()
input()
