t=eval(input("Enter values in tuple :"))
s=0
for i in t:
   s=s+i
   a=s/len(t)
print("Sum of tuple is :",s,"And Average of tuple is :",a)   
y=tuple(sorted(t))
print("Sorted tuple :",y)
   
input()
