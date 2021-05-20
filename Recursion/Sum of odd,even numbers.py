def Sum_odd(n):
    if n==1:
        return 1
    else:
        return 2*n-1 + Sum_odd(n-1)
def Sum_even(n):
    if n==0:
        return 0
    else:
         return 2*n + Sum_even(n-1)  
n=int(input("Enter the limit :"))
r=Sum_odd(n)
q= Sum_even(n)
print("Sum of Odd Number is :",r)
print("Sum of Even Number is :",q)
