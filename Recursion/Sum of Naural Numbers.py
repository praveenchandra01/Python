def Sum_N(n):
    if n==1:
        return 1
    else :
        return n+Sum_N(n-1)
n=int(input("Enter the limit :"))
r=Sum_N(n)
print("Sum is :",r)
