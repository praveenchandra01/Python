a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
y=min(a,b)
for i in range (2,y):
    if a%i==0 and b%i==0:
        print("Not a Co-prime")
        break
else:
    print("Numbers are Co-prime")
input()    
