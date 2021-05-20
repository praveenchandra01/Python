def Digi_Sum(n):
    if n==0:
        return 0
    else:
        return n%10+Digi_Sum(n//10)
    print("Sum of Digit is :",s)
n=int(input("Enter Number :"))
r=Digi_Sum(n)
print(r)
