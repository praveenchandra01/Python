for i in range(0,3):
    x=int(input("Enter the month in numeric format: "))
    while x<=12:
     
     if x%2!=0 and  x!=2 and x!=8:
            print("Number of days in month is 31")
            break
     elif x==2 :
             x=int(input("Enter year"))
             r="29 Days" if x%400==0 else "29days" if x%4==0 and x%100!=0 else "28 days"
             print(r)
             break
     elif x==8 :
                    print("31 days")
                    break
     
     else :
               print("Number of days in month is 30")
               break
    else :
          print("Please enter valid month")
input()
