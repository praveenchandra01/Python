q=int(input("Enter the question no."))

if q==1 :
    print("Print first 10 natural numbers")
    x=1
    while  x<=10 :
        print(x)
        x=x+1
            
elif q==2 :
    print("Print first 10 natural numbers in decreasing order")
    x=10
    while  x>=1 :
            print(x)
            x=x-1
            
elif q==3 :
    print("Print first 10 odd natural numbers")
    x=1
    while x<=19 :
         print (x)
         x=x+2
elif q==4 :
    print("Print first 10 even natural numbers")
    
    x=2
    while x<=20 :
         print (x)
         x=x+2
         
elif q==5 :
    print("Print first N natural numbers, value of N given by user")
    x=int(input("Enter the number :"))
    y=1
    while y<=x :
            print(y)
            y=y+1
            
elif q==6 :
   print("Print first N natural numbers in reverse order, value of N given by user") 
   x=int(input("Enter the number"))
   while x>=1 :
            print(x)
            x-=1
            
elif q==7 :
    print("To calculate sum of N natural numbers")
    x=int(input("Enter the number"))
    y=1
    s=0
    while y<=x :
            print(y)
            s=s+y
            y+=1
    print("Sum of natural numbers",s)
    
elif q==8 :
    print("To calculate sum of N odd natural numbers")
    x=int(input("Enter the number"))
    y=1
    s=0
    while y<=x :
            print(y)
            s=s+y
            y+=2
    print("Sum of natural numbers",s)
    
elif q==9 :
    print("Factorial of a given number")
    x=int(input("Enter a no. to find its factorial :"))
    fact=1
    if  x<0 :
            print("Factorial of negative number not possible")
    elif  x==0 :
            print("Factorial is 1")
    else :
        while x>=1 :
               fact=fact*x
               x=x-1
        print("Factorial is :",fact)
               
    
    
else :
    print("To calculate product of N odd natural numbers")
    x=int(input("Enter the number :"))
    y=1
    p=1
    while y<=x :
             print(y)
             p=p*y
             y=y+2
    print("Product is :",p)
     
input()     

