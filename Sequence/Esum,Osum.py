l=[]
n=int(input("Enter the length of list :"))
print("Enter the elements in list")
for i in range(n):
    x=int(input())
    l.append(x)
print(l)
esum=0
osum=0
i=0
while i<len(l):
    if l[i]%2==0:
        esum+=l[i]
    else:
        osum+=l[i]
    i+=1  
print("Sum of Even numbers in the list :",esum)
print("Sum of odd numbers in the list :",osum)
        
input()
