s=set([eval(e) for e in input("Enter elements in set :").split(",")])
'''print(len(s))'''
c=0
a=0
p=1
for i in s:
    c+=1
    a+=i
    p*=i
print("Number of elements in set :",c)
print("Product of elements",p)
print("Sum of elements",a)
input()
