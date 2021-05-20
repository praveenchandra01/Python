'''l=eval(input("Enter the numbers in list :"))'''
l=[]
n=int(input("Enter length of list :"))
for i in range(n):
    v=int(input("Enter Elements"))
    l.append(v)
print(l)
print("Unsorted List :",l)
l.sort()
print("Sorted List :",l)
print("Greatest no. in list :",max(l))
s=0
for i in l:
    s+=i
print("Sum of values of list :",s)
input()
