class Stuedent:
    def __init__(self,name,rollno,sem,branch,x,y,z):
        self.Name=name
        self.Rollno=rollno
        self.Semester=sem
        self.Branch=branch
        self.m1=x
        self.m2=y
        self.m3=z
        
    def Display(self):  #instance member funtion
        print("\n\nStudent Details :")
        print("Name :",self.Name)
        print("Roll Number :",self.Rollno)
        print("Semester :",self.Semester)
        print("Branch :",self.Branch)
    
    def Percentage(self):
        p=((m1+m2+m3)/300)*100
        print("Percentage :",p,'%')
        return p
        
    def Grade(self):
        x=self.Percentage()
        if x>=90:
            print("Grade A")
        elif x<90 and x>=80:
            print("Grade B")
        else:
            print("Grade C")
        
name=input("Enter the Name :")
rollno=int(input("Enter the Roll no. :"))
sem=input("Enter the Semester :")
branch=input("Enter the Branch :")
m1=int(input("Enter your First subject marks :"))
m2=int(input("Enter your Second subject marks :"))
m3=int(input("Enter your Third subject marks :"))
       
S1=Stuedent(name,rollno,sem,branch,m1,m2,m3)
S1.Display()
S1.Grade()
input()
