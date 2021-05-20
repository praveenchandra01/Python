x=int(input("Enter first number :"))
y=int(input("Enter second number :"))
z=x if x>y else y
print("Greatest value is :",z)


x=int(input("Enter a year :"))
r="Leap year" if x%400==0 else "Leap year" if x%4==0 and x%100!=0 else "Non leap year"
print(r)
input()
