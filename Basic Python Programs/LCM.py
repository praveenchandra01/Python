a=int(input("Enter First number :"))
b=int(input("Enter Second number :"))
for i in range (1,a*b+1):
     if i%a==0 and i%b==0 :
         print("LCM is :",i)
         break
input()
