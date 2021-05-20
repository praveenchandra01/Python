def nxt_prime(x):
   
    while 1:
         x=x+1
         for i in range(2,x):
              if x%i==0:
                  break
         else:
            return x
            break
n=int(input("Enter number :"))
r=nxt_prime(n)
print(r)
input()
