n=int(input("Enter the no."))
s=0
x=n
while x!=0 :
        r=x%10
        s=s+r**3
        x=x//10

if s==n:
    print("Armstrong no. ")
else :
    print("Not a Armstrong no.")
input()
    
print("Armstrong numbers are :")
for n in range(1,1001):
    s=0
    x=n
    while x!=0 :
        r=x%10
        s=s+r**3
        x=int(x/10)
    if s==n:
        print(n)
input()        
            
        


            
    
