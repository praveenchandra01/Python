t1=eval(input("Enter elemants in tuple 1 :"))
t2=eval(input("Enter elemants in tuple 2 :"))
x=tuple(sorted(t1))
y=tuple(sorted(t2))
print(x+y)
r=t1[::-1]
print("Tuple t1 in reverse order :",r)
print(type(t1))
input()
