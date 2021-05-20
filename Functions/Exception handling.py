#case1 :Python,DEM
x=int(input("Enter first number :"))
y=int(input("Enter second number :"))
z=x/y 
print(z)
#case2: Python,EM
x=int(input("Enter first number :"))
y=int(input("Enter second number :"))
try:
    z=x/y
    print(z)
except ZeroDivisionError:
    print("Invalid zero division not possible")

#case 3: User,DEM
x=int(input("Enter first number :"))
y=int(input("Enter second number :"))
if y==0:
    raise ZeroDivisionError ("Denominator can't be zero")
z=x/y
print("Division",z)

#case4:User,EM
x=int(input("Enter first number :"))
y=int(input("Enter second number :"))
try:
    if y==0:
        raise ZeroDivisionError ("Denominator can't be zero")
    z=x/y
    print("Division",z)
except ZeroDivisionError:
    print("invalid")
input()
