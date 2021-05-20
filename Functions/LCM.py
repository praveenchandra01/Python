def LCM(x,y):
    for i in range(1,x*y+1):
        if i%x==0 and i%y==0:
            return i
a,b=int(input("Enter first number :")),int(input("Enter second number :"))
s=LCM(a,b)
print("LCM is :",s)        
input()            
