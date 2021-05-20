def Fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Fact(n-1)
N=int(input("Enter a Number to find its Factorial :"))
r=Fact(N)
print("Factorial is :",r)    
