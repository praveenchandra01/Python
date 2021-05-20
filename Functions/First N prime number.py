def Prime_N(n):
    x=2
    while  n!=0:
        for i in range(2,x):
          if x%i==0:
              break
        else:
              print(x)
              n-=1
        x+=1
n=int(input("Enter limit :"))
Prime_N(n)
input()

