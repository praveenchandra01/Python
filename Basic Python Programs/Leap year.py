x=int(input("Enter a year to cheak wheather it is leap year or not :"))
if x%400==0 :
      print("The year %d is leap year" %x)
elif x%4==0 and x%100!=0 :
     print("Leap year")
else :
     print("Not a leap year")
input()
