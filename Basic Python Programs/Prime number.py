n=int(input("Enter a number :"))
if n<2 :
    print("Not a Prime number")
else :
    for i in range(2,n) :
        if n%i==0 :
             print("Not a Prime number")
             break
    else :
          print("Prime Number")
input()          
