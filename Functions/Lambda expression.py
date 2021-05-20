s=lambda a,b:a+b
r=s(10,20)
print("Sum is :",r)

r=(lambda a,b:a+b)(10,20)
print("Sum is :",r)

r=(lambda a,b: a if a>b else b)(100,30)
print("Max value :",r)

print("Enter two numbers :")
r=(lambda a,b: a if a>b else b)(int(input()),int(input()))
print("Max value :",r)

f=lambda a:1 if a==0 or a==1  else a*f(a-1)
print("factorial is :",f(5))
