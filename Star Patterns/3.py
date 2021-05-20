n=int(input("Enter number of rows :"))
for i in range(0,n+1):
    for j in range(n+1):
        if j<=n-i:
            print("*",end=' ')
        else:
            print("",end=' ')
    print()
input()
            
