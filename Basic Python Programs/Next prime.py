n=int(input("Enter the number :"))
while 1 :
    n+=1
    for i in range (2,n) :
        if n%i==0 :
            break
    else :
            print("Prime number",n)
            break
input()    

