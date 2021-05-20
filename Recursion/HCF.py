def HCF(a,b):
    r=a%b
    if r==0:
        return b
    else:
       return HCF(b,r)


a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
r=HCF(a,b)
print("HCF of %d  and %d is %d"%(a,b,r))
input()
