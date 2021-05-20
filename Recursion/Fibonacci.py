def Fibo(n):
    if n==0 or n==1:
        return n
    else:
        return Fibo(n-1)+Fibo(n-2)
n=int(input("Enter how many number of fibonacci seris you want to :"))
if n<=0:
    print("Enter Positive Integer ")
else:    
   for i in  range(n):
        print(Fibo(i),end=' ')

input()
