a=int(input("Enter the marks of five subjects\nMathematics :"))
b=int(input("Physics :"))
c=int(input("Chemistry :"))
d=int(input("English :"))
e=int(input("Computer Science :"))
p=((a+b+c+d+e)/500)*100
if p>33 :
        print("PASS your percentage is=",p,"%")
        if d>75 :
            print("Distinction")
        elif d>65 :
            print("1st Dividion")
        elif d>55 :
            print("2nd Division")
        else  :
            print("3rd Division")
else :
    print("FAIL")
input("Press enter to exit")
