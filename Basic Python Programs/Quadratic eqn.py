import math as m
a=float(input("Enter the coefficient a="))
b=float(input("Enter the coefficient b="))
c=float(input("Enter the coefficient c="))
d=(b**2) -(4*a*c)
if d>0 :
    r1=(-b+m.sqrt(d))/(2*a)
    r2=(-b-m.sqrt(d))/(2*a)
    print("Roots are real and distinct \nroot 1=",r1,"\nroot 2=",r2)
    input()
elif d==0 :
     r1=(-b/(2*a))
     print("Roots are real and same",r1, "and" ,r1)
     input()
else :
 print("No real root exist")
 input()

        
