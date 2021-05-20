import math as m
a=int(input("Enter number 1 :"))
b=int(input("Enter number 2 :"))
if m.gcd(a,b)==1 :
    print("Numbers %d  and %d are Co-prime"%(a,b))
else:
    print("Not a Co-prime")
input()    
            
