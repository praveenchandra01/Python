a=int(input("Enter smaller number :"))
b=int(input("Enter greater number :"))
for x in range(a,b):
    if x!=0 and x!=1:  
      for i in range(2,x):
            if x%i==0:
               break
      else:
            print(x)
input()        

'''
a=int(input("Enter smaller number :"))
b=int(input("Enter greater number :"))
s=range(a,b)
for x in s :
    for n in range(2,x):
        if x%n==0 :
            break
    else :
        print(x,"is prime number in range")
        break
    print(x)
input()
'''
