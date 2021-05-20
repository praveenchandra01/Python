s1=set([eval(i) for i in input("Enter elements in Set 1:").split(',')])
s2=set([eval(i) for i in input("Enter elements in Set 2:").split(',')])
a=s1.union(s2)
b=s1.intersection(s2)
c=s2.issubset(s1)
if c==True:
    print('Set s2 is a Subset of Set s1')
print("Union:",a,"\nIntersection:",b)
input()
