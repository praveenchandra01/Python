n=int(input("Enter the no. of Rows :"))
for i in range(0,n):
    for j in range(0,n+1):
        if j>=n-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()    
input()
