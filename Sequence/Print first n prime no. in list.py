n=int(input("Enter the value of N :"))
l=[]
x=2
while n!=0:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        l.append(x)
        n-=1
    x+=1
print(l)

n=int(input("Enter the value of N :"))
l=[]
x=2
while n!=0:
    flag=0
    for i in range(2,x):
        if x%i==0:
            flag=1
            break
    if flag==0:
        l.append(x)
        n-=1
    x+=1
print(l)
input()        
