a=int(input("Enter first number :"))
b=int(input("Enter  second number :"))
y=min(a,b)
for i in range(y,1,-1):
    if a%i==0 and b%i==0:
        print (i)
        break
input()
