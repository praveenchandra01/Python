x=int(input("Enter the the month in numeric format: "))
if x%2==0 and x!=1 and  x!=2 and x!=7 :
    print("Number of days in month is 31")
elif x==2 :
    x=int(input("Enter  year  :"))
    if x%400==0 :
      print("29 Days")
    elif x%4==0 and x%100!=0 :
     print("29 Days")
    else :
     print("28 Days")
elif x==7 :
    print("31 days")
elif x==1:
        print("31 Days")
else :
    print("Number of days in month is 30")
input()
'''
x=int(input("Enter the month in numeric format: "))
if x%2==0 and x!=2 and  x!=7 :
    print("Number of days in month is 31")
elif x==2 :
 x=int(input("Enter year"))
 r="29 Days" if x%400==0 else "29days" if x%4==0 and x%100!=0 else "28 days"
 print(r)
elif x==7 :
    print("31 days")
else :
    print("Number of days in month is 30")
    input()
    '''
