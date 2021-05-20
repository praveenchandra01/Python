def PrintN_even(n):
    if n!=0:
        PrintN_even(n-1)
        print(2*n,end=' ')
def PrintN_evenRev(n):
    if n>0:
        print(2*n,end=' ')
        PrintN_evenRev(n-1)

def PrintN_odd(n):
    if n!=0:
        PrintN_odd(n-1)
        print(2*n-1,end=' ')
def PrintN_oddRev(n):
    if n>0:
        print(2*n-1,end=' ')
        PrintN_oddRev(n-1)        
N=int(input("Enter the limit :"))
PrintN_even(N)
print("...Even Numbers")
PrintN_evenRev(N)
print('...Even numbers in Reverse order ')
PrintN_odd(N)
print("...Odd Numbers")
PrintN_oddRev(N)
print("...Odd numbers in Reverse order")
