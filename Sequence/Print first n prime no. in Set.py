n=int(input("Enter the limit :"))
s=set()
x=2;
while n!=0:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        s.add(x)
        n-=1
    x+=1
print(s)        
input()
