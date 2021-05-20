def Permutation(n,r):
        return fact(n)//fact(n-r)
def Combination(n,r):
        return fact(n)//(fact(n-r)*fact(r))
def fact(n):
    if n==1:
        return 1
    else:
       return n*fact(n-1)

a=int(input("Enter the value of n :"))
b=int(input("Enter the value of r :"))
P=Permutation(a,b)
C=Combination(a,b)
print("Permutation :",P)
print("Combination :",C)
input()
