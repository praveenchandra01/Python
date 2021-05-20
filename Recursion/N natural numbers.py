def PrintN(N,a):
    if N>=a:
        print(a)
        return PrintN(N,a+1)
def PrintN_rev(N):
    if N>0:
        print(N)
        PrintN_rev(N-1)
        
N=int(input("Enter the limit :"))
r=PrintN(N,a=1)
print(r)
print("In Reverse order :")
PrintN_rev(N)

input()
