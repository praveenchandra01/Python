def fibo_series(x):
    a=0
    b=1
    s=[]
    s.append(0)
    s.append(1)
    for i in range(x):
        c=a+b
        a=b
        b=c
        s.append(c)
    return s  
N=int(input("Enter nth term of Fibonacci series :"))
r=fibo_series(N-2)
print("Fibpnacci Series :")
print(r)
input()
