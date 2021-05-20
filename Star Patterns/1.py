n=int(input("Enter the no. of Rows :"))
for i in range(n):
    for j in range(n):
        if j<=i:
            print("*",end=" ")
    print()    
input()
